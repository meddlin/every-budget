from flask import Flask, Blueprint, request, jsonify
from flask import current_app as app
from flask_cors import cross_origin

budgets_bp = Blueprint(
    'budgets_bp', __name__
)


@cross_origin()
@budgets_bp.route('/get/<budget_id>', methods=['GET', 'POST'])
def get(budget_id):
    print(budget_id)
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@budgets_bp.route('/create', methods=['POST'])
def create(budget):
    content = request.json
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@budgets_bp.route('/update', methods=['POST'])
def update(budget):
    return ''


@cross_origin()
@budgets_bp.route('/delete/<budget_id>', methods=['POST'])
def delete(budget_id):
    return ''