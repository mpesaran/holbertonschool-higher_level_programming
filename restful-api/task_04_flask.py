#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """homepage"""
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=['GET'])
def get_data():
    """Fetch and list username is user"""
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=['GET'])
def get_status():
    """return status page"""
    return "OK", 200


@app.route("/users/<username>", methods=['GET'])
def get_user(username):
    """Fetches specific user from user dictionary"""
    user = users.get(username)
    if user:
        user_complete = {
            "username": username,
            **user
        }
        return jsonify(user_complete), 200
    return jsonify({'error': 'User not found'}), 400


@app.route("/add_user", methods=['POST'])
def add_new_user():
    """post data to add_user endpoint and returns a response"""
    data = request.get_json()
    if not data or 'username' not in data or 'name' not in data:
        return jsonify({'error': 'Username is required'}), 400
    username = data['username']
    users[username] = {
        'name': data['name'],
        'age': data['age'],
        'city': data['city']
    }
    return jsonify({'message': 'User added', 'user': data}), 201


if __name__ == "__main__":
    app.run()
