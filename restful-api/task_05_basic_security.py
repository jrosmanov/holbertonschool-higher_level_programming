from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'fYLv51a4aDURpIkGdBqUCBBv6rk'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# """database"""
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    if not user or 'username' not in user or 'password' not in user:
        return jsonify({'error': 'Invalid Credentials'}), 401

    username = user.get('username')
    password = user.get('password')
    role = users[username]['role']

    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': role})
        return jsonify(access_token=access_token)
    return jsonify({'error': 'Wrong data'}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected():
    return 'JWT Auth: Access Granted'


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def check_admin():
    data = get_jwt()
    if data['sub'].get('role') != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    return 'Admin Access: Granted'
