from flask import jsonify
from app import app
from app.services import add_number, get_number, get_all


@app.route('/add/<num>', methods=['POST'])
def add(num):
    try:
        num = int(num)
        return jsonify(add_number(num))
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter a number."})


@app.route('/get_one/<num>', methods=['GET'])
def get(num):
    try:
        num = int(num)
        return jsonify(get_number(num))
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter a number."})


@app.route('/get_all', methods=['GET'])
def get_all_route():
    return jsonify(get_all())