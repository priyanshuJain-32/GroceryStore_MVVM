# ========================= Library Imports ============================
from flask import Blueprint, request

# ========================= Local Imports ============================
from ..celery_files import tasks
from ..decorators.admin_deco import admin_required
from ..decorators.token_deco import token_required

jobs = Blueprint('jobsApi',__name__)

# ==========================================================================
# #========================== Jobs API =====================================
# ==========================================================================


# @token_required
# @admin_required
@jobs.route("/notification", methods=['GET'])
def notification(email, status):
    job = tasks.notification(email, status)
    return str(job), 200

@jobs.route("/test", methods=['GET'])
def test():
    job = tasks.send_monthly_report()
    return str(job), 200