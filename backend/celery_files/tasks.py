from datetime import datetime
from celery.schedules import crontab

from ..api.reportApi import analytics
from ..mail_server.mail_service import send_email 
from .workers import celery
from ..models.user import Users
from ..models.product import Product
from ..models.requests import Requests
from ..models.order import Orders

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Reminder for visiting back to customers who logged in >24 hours back
    sender.add_periodic_task(crontab(hour=10), 
                            send_revisit_reminder.s(), 
                            name='Monthly Report')
    
    # Reminder to admin for requests sitting in dashboard at 10:00 am everyday
    sender.add_periodic_task(crontab(hour=10), 
                            send_request_reminder.s(), 
                            name='Monthly Report')
    
    # Monthly activity report to admin and manager
    sender.add_periodic_task(crontab(hour = 10, day_of_month=1),
                             send_monthly_report.s(),
                             name = 'Monthly Report')

# User specific
@celery.task()
def send_revisit_reminder(*args, **kwargs):
    users = Users.query.filter_by(role='user')
    content_body = '''
    <html>
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
    '''
    for user in users:
        if (datetime.now() - user.last_login).total_seconds()/3600>24:
            send_email(user.email, "Forgot us, here is a deal", content_body)
    return "Sent", 200


# Admin specific
@celery.task()
def send_request_reminder(*args, **kwargs):
    user = Users.query.filter_by(role='admin').first()
    content_body = '''
    <html>
        <body>
            <h1> 
                There are pending requests.
            </h1>
            <p>
                Please visit Admin Dashboard and resolve them.
            </p>
        </body>
    </html>
    '''
    requests = Requests.query.filter_by(request_status = 'pending').all()
    if requests:
        send_email(user.email, "Resolve pending requests reminder", content_body)
        return "Sent", 200
    else:
        return "Nothing pending", 200
    

@celery.task()
def send_monthly_report():
    user = Users.query.filter_by(role='admin').first()
    date = datetime.today().date()
    category_names, category_sales = analytics(user)
    content_body = '''
    <html>
        <body>
            <h1>
                Monthly Report
            </h1>
            <ul>
            {% for category, sales in zip(category_names, category_sales) %}
                <li>{{ category }} {{ sales }}</li>
            </ul>
        </body>
    </html>
    '''

    send_email(user.email, "Monthly Report {}".format(date) ,content_body)
    return "Sent", 200



@celery.task()
def notification(email, status):
    content_body_success = '''
    <html>
        <body>
            <h2>
                Your request has been approved.
            </h2>
        </body>
    </html>
    '''
    content_body_failure = '''
    <html>
        <body>
            <h2>
                Your request has been rejected. If you think it was a mistake contact Admin.
            </h2>
        </body>
    </html>
    '''
    if status=="approve":
        send_email(email, "Signup successful", content_body_success)
        return "Success", 200
    else:
        send_email(email, "Signup request rejected", content_body_failure)
        return "Rejected", 200