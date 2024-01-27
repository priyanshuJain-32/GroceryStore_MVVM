# ========================= Library Imports ============================
from flask import Blueprint, request, jsonify, send_file

# ========================= Local Imports ============================
from ..celery_files import tasks
from ..decorators.admin_deco import admin_required
from ..decorators.token_deco import token_required
from ..celery_files.tasks import export_products, export_categories, export_orders, export_users
from celery.result import AsyncResult # This had bugs
import os

jobs = Blueprint('jobsApi',__name__)

# ==========================================================================
# #========================== Jobs API =====================================
# ==========================================================================

@jobs.route("/notification/<email>/<status>", methods=['GET'])
def notification(email, status):
    job = tasks.notification(email, status)
    return str(job), 200

@jobs.route("/test", methods=['GET'])
def test():
    job = tasks.send_monthly_report()
    return (job), 200

@jobs.route("/generate_csv/<for_what>", methods=['GET'])
@token_required
@admin_required
def generate_csv(user,for_what):
    if for_what=="products":
        task = export_products.delay()
    elif for_what == "categories":
        task = export_categories.delay()
    elif for_what == "users":
        task = export_users.delay()
    elif for_what == "orders":
        task = export_orders.delay()
    return jsonify({"task_id": task.id})

@jobs.route("/get_csv/<task_id>/<for_what>", methods=['GET'])
@token_required
@admin_required
def get_csv(user, task_id, for_what):
    folder_path = os.path.join(os.getcwd(), 'project/static')
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            if (file.split(".")[0]=='products_export' and for_what == "products"):
                file_path = folder_path+"/"+file
                response = send_file(file_path, as_attachment=True, download_name='data.csv')
                os.remove(file_path)
                return response
            
            elif (file.split(".")[0]=='categories_export' and for_what == "categories"):
                file_path = folder_path+"/"+file
                response = send_file(file_path, as_attachment=True, download_name='data.csv')
                os.remove(file_path)
                return response
            
            elif (file.split(".")[0]=='orders_export' and for_what == "orders"):
                file_path = folder_path+"/"+file
                response = send_file(file_path, as_attachment=True, download_name='data.csv')
                os.remove(file_path)
                return response
            
            elif (file.split(".")[0]=='users_export' and for_what == "users"):
                file_path = folder_path+"/"+file
                response = send_file(file_path, as_attachment=True, download_name='data.csv')
                os.remove(file_path)
                return response
    return jsonify({"message": "File not found"}), 404

@jobs.route("/get_csv/<task_id>", methods=['GET'])
def get_csv_async(task_id, for_what):
    folder_path = os.path.join(os.getcwd(), 'project/static')
    res = AsyncResult(task_id)

    if res.ready():
        filename = res.result
        return send_file(folder_path + filename, as_attachment=True)
    else:
        return jsonify({"message": "Task pending"}), 404
    