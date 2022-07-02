from flask import Flask, Blueprint, request, jsonify
from flask import current_app as app
from flask_cors import cross_origin

envelopes_bp = Blueprint(
    'envelopes_bp', __name__
)


@cross_origin()
@envelopes_bp.route('/get/<envelope_id>', methods=['GET', 'POST'])
def get(envelope_id):
    print(envelope_id)
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@envelopes_bp.route('/create', methods=['POST'])
def create(envelope):
    content = request.json
    return ''


## TODO : Pass budget JSON-body to this method
@cross_origin()
@envelopes_bp.route('/update', methods=['POST'])
def update(envelope):
    return ''


@cross_origin()
@envelopes_bp.route('/delete/<envelope_id>', methods=['POST'])
def delete(envelope_id):
    return ''