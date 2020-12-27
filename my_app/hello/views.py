from flask import jsonify, Blueprint

hello = Blueprint('hello', __name__)
@hello.route('/')

def index():
    return jsonify({'name': '123'})