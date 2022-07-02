from flask import Flask, Blueprint, request, jsonify
from flask import current_app as app
from flask_cors import cross_origin

transactions_bp = Blueprint(
    'transactions_bp', __name__
)


@cross_origin()
@transactions_bp.route('/get/<transaction_id>', methods=['GET', 'POST'])
def get(transaction_id):
    print(transaction_id)
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@transactions_bp.route('/create', methods=['POST'])
def create(transaction):
    content = request.json
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@transactions_bp.route('/update', methods=['POST'])
def update(transaction):
    return ''


@cross_origin()
@transactions_bp.route('/delete/<transaction_id>', methods=['POST'])
def delete(transaction_id):
    return ''