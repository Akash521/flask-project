# app/routes/user_routes.py
from flask import Blueprint, jsonify

# Create a Blueprint object
user_routes = Blueprint('user_routes', __name__)

# Define your route
@user_routes.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "User list will be here!"})

# Define the /users/<username> route
@user_routes.route('/users/<username>', methods=['GET'])
def get_user(username):
    users = {
        "akash": {"email": "akash@example.com", "age": 25},
        "john": {"email": "john@example.com", "age": 30}
    }
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Define your route
@user_routes.route('/users/greetings', methods=['GET'])
def get_users():
    return jsonify({"message": "Hello How are you all people"})