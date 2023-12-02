# 
from flask import Blueprint, request, jsonify

from .. import db
from ..models.user import Users
from ..models.requests import Requests
from ..decorators.staff_deco import staff_required
from ..decorators.token_deco import token_required
from ..decorators.admin_deco import admin_required

request = Blueprint('requestApi', __name__)

@request.route('/get_request', methods=['GET'])
@token_required
@staff_required
def get_request(user):
    requests = Requests.query.filter_by(requester_id = user.user_id).all()
    request_list = []
    if not requests:
        return jsonify({'message':'No pending requests'}), 200
    for request in requests:
        request_list.append({
            'request_id': request.request_id,
            'requester_id': request.requester_id,
            'request_type': request.request_type,
            'request_status': request.request_status})
    return jsonify(request_list), 200

@request.route('/submit_request', methods=['POST'])
@token_required
@staff_required
def submit_request(user):
    data = request.get_json()

    requester_id_ = user.user_id
    request_type_ = data['request_type']

    new_request = Requests(
        requester_id = requester_id_,
        request_type = request_type_)
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message':'Submitted successfully'}), 200

################# Admin Controls ###############################

@request.route('/get_all_request', methods=['GET'])
@token_required
@admin_required
def get_all_request(user):
    requests = Requests.query.all()
    request_list = []
    if not requests:
        return jsonify({'message':'No pending requests'}), 200
    for request in requests:
        request_list.append({
            'request_id': request.request_id,
            'requester_id': request.requester_id,
            'request_type': request.request_type,
            'request_status': request.request_status})
    return jsonify(request_list), 200

@request.route('/alter_request_status', methods = ['PUT'])
@token_required
@admin_required
def alter_request_status(user):
    data = request.get_json()

    request = Requests.query.filter_by(request_id= data.request_id).first()
    if request.request_type == 'signup':
        request.request_status = data.request_status
        
        if data.request_status == 'approve':
            requester_user = Users.query.filter_by(user_id=request.requester_id).first()
            requester_user.status = 'active'
            db.session.commit()
            return jsonify({'message': 'Manager Signup completed'}), 200
            
    request.request_status = data.request_status
    db.session.commit()
    return jsonify({'message': 'Altered status successfully'}), 200

@request.route('/delete_request/<int:request_id>', methods = ['DELETE'])
@token_required
@admin_required
def delete_request(user, request_id):
    request = Requests.query.filter_by(request_id= request_id).first()
    if not request:
        return jsonify({'message': 'Request not found'}), 404
    db.session.delete(request)
    db.session.commit()
    return jsonify({'message': 'Deleted request successfully'}), 200