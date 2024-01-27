from datetime import datetime
from celery.schedules import crontab
import flask_excel as excel
import csv
import os
from pyhtml import html, head, link, body, h1, h2, h3, h4, p, table, tr, th, td, hr, style

from ..api.reportApi import analytics
from ..mail_server.mail_service import send_email 
from .workers import celery
from ..models.user import Users
from ..models.product import Product
from ..models.category import Category
from ..models.order import Orders
from ..models.user import Users
from ..models.requests import Requests
from ..models.order import Orders
from ..static.styles import style_css

#============================CRON NOTIFICATIONS==========================

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Reminder for visiting back to customers who logged in >24 hours back
    sender.add_periodic_task(crontab(minute=54, hour=11), 
                            send_revisit_reminder.s(), 
                            name='Monthly Report')
    
    # Reminder to admin for requests sitting in dashboard at 10:00 am everyday
    sender.add_periodic_task(crontab(minute=50), 
                            send_request_reminder.s(), 
                            name='Monthly Report')
    
    # Monthly activity report to admin and manager
    sender.add_periodic_task(crontab(minute=59, hour=11), # Excluded day_of_month for demo
                             send_monthly_report.s(),
                             name = 'Monthly Report')

# ==============================USER SPECIFIC NOTIFICATIONS======================
@celery.task()
def send_revisit_reminder(*args, **kwargs):
    users = Users.query.filter_by(role='user')
    content_body = '''
    <html>
    <style>
        {}
    </style>
        <body>
            <h1> 
                Great deals are waiting for you.
            </h1>
            <p>
                This christmas gift yourself a new iPhone with great deals from Shoppers dont stop.
                We are offering some great deals just for you.
            </p>
        </body>
    </html>
    '''.format(style_css)
    for user in users:
        if (datetime.now() - user.last_login).total_seconds()/3600>24:
            send_email(user.email, "Forgot us, here is a deal", content_body)
    return "Sent", 200


# =============================EMAIL NOTIFICATIONS===================================
@celery.task()
def send_request_reminder(*args, **kwargs):
    user = Users.query.filter_by(role='admin').first()
    content_body = '''
    <html>
    <style>
        {}
    </style>
        <body>
            <h1> 
                There are pending requests.
            </h1>
            <p>
                Please visit Admin Dashboard and resolve them.
            </p>
        </body>
    </html>
    '''.format(style_css)
    requests = Requests.query.filter_by(request_status = 'pending').all()
    if requests:
        send_email(user.email, "Resolve pending requests reminder", content_body)
        return "Sent", 200
    else:
        return "Nothing pending", 200
    

@celery.task()
def send_monthly_report():
    
    date = datetime.today().date()
    category_data = Category.query.all()
    category_tuple = []
    product_tuple = []
    inventory_tuple = []

    for category in category_data:
        category_total = 0
        for product in category.products:	
            product_total = 0
            inventory_tuple.append((product.product_id,
                                    product.cost_price, 
                                    product.sell_price, 
                                    product.discount, 
                                    product.product_quantity, 
                                    product.expiry_date))
            for order in product.orders:
                category_total += order.order_quantity*product.sell_price*(100-product.discount)/100
                product_total += order.order_quantity*product.sell_price*(100-product.discount)/100
            product_tuple.append((product_total, product.product_name))
        category_tuple.append((category_total, category.category_name))
    product_tuple.sort(reverse=True)
    category_tuple.sort(reverse=True)
    
    total_revenue = 0
    for value,product in product_tuple:
        total_revenue += value
    

    users = Users.query.filter_by(role='user').all()
    user_count = len(users)

    def generate_table_rows(data):
        return [tr(td(item[1]), td(item[0])) for item in data]
    
    def generate_three_table_rows(data):
        return [tr(td(item[1]), td(item[2]), td(item[0])) for item in data]

    def calculate_inventory(data):
        inventory_val = 0
        for (id, cost, sell, dis, quan, exp) in data:
            inventory_val += cost*quan
        return inventory_val
    
    def perishable_non_perishable(data):
        perishable_count, perishable_value = 0, 0
        non_perishable_count, non_perishable_value = 0, 0
        for (id, cost, sell, dis, quan, exp) in data:
            if (exp!='' and exp!=None):
                non_perishable_count += 1
                non_perishable_value += quan*cost
            else:
                perishable_count += 1
                perishable_value += quan*cost
        return [perishable_count, perishable_value, non_perishable_count, non_perishable_value]
    
    def top_ten_users(data):
        user_order_value = []
        user_order_count = []
        
        for user in data:
            order_value = 0
            order_count = 0
            for order in user.orders:
                order_count += 1
                order_value += order.order_sell_price*(100-order.order_discount)/100*order.order_quantity
            user_order_value.append((order_value, user.user_id, user.name))
            user_order_count.append((order_count, user.user_id, user.name))
        user_order_value.sort()
        user_order_count.sort()
        return [user_order_value, user_order_count]
    
    # HTML content generation
    t = html(
        head(
            style(style_css)
            ),
            body(
                h2("Monthly Report - December 2023"),
                
                h3("INVENTORY REPORT"),
                
                h3("Total Inventory Value"),
                p("Value : "+ str(calculate_inventory(inventory_tuple)) + "₹"),

                h3("Inventory split"),
                p("Perishables : " + str(perishable_non_perishable(inventory_tuple)[0])),
                p("Perishables Value : " + str(perishable_non_perishable(inventory_tuple)[1]) + "₹"),
                p("Non-Perishables : " + str(perishable_non_perishable(inventory_tuple)[2])),
                p("Non-Perishables Value : " + str(perishable_non_perishable(inventory_tuple)[3]) + "₹"),

                hr(),

                h3("USER REPORT"),
                
                p(f"Total Users: {user_count}"),
                p(f"Top 10 customers by order value: "),
                table(
                    tr(th("User Id"), th("User Name"), th("Total Orders Value")),
                    *generate_three_table_rows(top_ten_users(users)[0])
                ),
                p(f"Top 10 customers by # of orders: "),
                table(
                    tr(th("User Id"), th("User Name"), th("Total #of Orders")),
                    *generate_three_table_rows(top_ten_users(users)[1])
                ),

                hr(),

                h3("REVENUE REPORT"),
                
                h3("Total Revenue Value (in INR)"),
                p("Value: "+ str(total_revenue)),

                h3("Revenue Split"),
                h3("Category Sales"),
                table(
                    tr(th("Category Name"), th("Sales Amount")),
                    *generate_table_rows(category_tuple)
                ),

                h3("Product Sales"),
                table(
                    tr(th("Product Name"), th("Sales Amount")),
                    *generate_table_rows(product_tuple)
                ),
            )
    )
    
    content_body = t.render()
    user = Users.query.filter_by(role='admin').first()
    send_email(user.email, "Monthly Report {}".format(date) ,content_body)
    return "Sent"

# ================================API Triggered notification==================
@celery.task()
def notification(email, status):
    content_body_success = '''
    <html>
        <style>
            {}
        </style>
        <body>
            <h2>
                Your request has been approved.
            </h2>
        </body>
    </html>
    '''.format(style_css)
    content_body_failure = '''
    <html>
        <style>
            {}
        </style>
        <body>
            <h2>
                Your request has been rejected. If you think it was a mistake contact Admin.
            </h2>
        </body>
    </html>
    '''.format(style_css)
    if status=="approve":
        send_email(email, "Request accepted successfully", content_body_success)
        return "Success", 200
    else:
        send_email(email, "Request rejected", content_body_failure)
        return "Rejected", 200

# ===================EXPORT TASKS===================================
@celery.task()
def export_products():
    products = Product.query.all()
    folder_path = os.path.join(os.getcwd(), 'project/static')

    # Create a temporary CSV file in the specified folder
    filename = os.path.join(folder_path, "products_export.csv")

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        columns = ["product_id",
               "product_name",
               "product_desc",
               "sell_price",
               "cost_price",
               "unit_of_measurement",
               "discount",
               "product_quantity",
               "expiry_date"]
        writer.writerow(columns)
        for product in products:
            writer.writerow([product.product_id, 
                             product.product_name, 
                             product.product_desc, 
                             product.sell_price, 
                             product.cost_price,
                             product.unit_of_measurement,
                             product.discount,
                             product.product_quantity,
                             product.expiry_date])
    return filename

@celery.task()
def export_categories():
    categories = Category.query.all()

    folder_path = os.path.join(os.getcwd(), 'project/static')

    # Create a temporary CSV file in the specified folder
    filename = os.path.join(folder_path, "categories_export.csv")


    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        columns = ["category_id",
                   "category_name"]
        writer.writerow(columns)
        for category in categories:
            writer.writerow([category.category_id,
                             category.category_name])
    return filename

@celery.task()
def export_orders():
    orders = Orders.query.all()

    folder_path = os.path.join(os.getcwd(), 'project/static')

    # Create a temporary CSV file in the specified folder
    filename = os.path.join(folder_path, "orders_export.csv")
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        columns = ["order_id",
                   "order_quantity", 
                   "sell_date",
                   "order_user_id",
                   "order_product_id",
                   "order_product_name",
                   "order_product_desc",
                   "order_sell_price",
                   "order_cost_price",
                   "order_unit_of_measurement",
                   "order_discount",
                   "order_expiry_date"]
        writer.writerow(columns)
        for order in orders:
            writer.writerow([order.order_id, 
                             order.order_quantity, 
                             order.sell_date, 
                             order.order_user_id, 
                             order.order_product_id,
                             order.order_product_name,
                             order.order_product_desc,
                             order.order_sell_price,
                             order.order_cost_price,
                             order.order_unit_of_measurement,
                             order.order_discount,
                             order.order_expiry_date])
    return filename

@celery.task()
def export_users():
    users = Users.query.all()

    folder_path = os.path.join(os.getcwd(), 'project/static')

    # Create a temporary CSV file in the specified folder
    filename = os.path.join(folder_path, "users_export.csv")
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        columns = ["user_id",
                   "name", 
                   "user_name",
                   "email",
                   "password",
                   "role",
                   "status",
                   "last_login"]
        writer.writerow(columns)
        for user in users:
            writer.writerow([user.user_id, 
                             user.name, 
                             user.user_name, 
                             user.email, 
                             user.password,
                             user.role,
                             user.status,
                             user.last_login])
    return filename