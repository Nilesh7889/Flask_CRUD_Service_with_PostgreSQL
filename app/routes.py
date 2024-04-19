from app import app
from flask import request, jsonify
from app import app, db
from datetime import datetime
from app.models import User


@app.route('/')
def index():
    return 'Authorization Service'


# Create new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(full_name=data['full_name'], email=data['email'], creation_date=datetime.now(),
                    services=data['services'])
    db.session.add(new_user)
    try:
        if new_user.full_name == "":
            return jsonify({'error message': 'Name can not be empty'}), 400
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        s = str(e)
        if 'duplicate key value violates unique constraint' in s:
            return jsonify({'error message': 'This email is duplicate, please try different email address.'}), 400
        else:
            return jsonify({'error': str(e)}), 400


# Get user by user ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'full_name': user.full_name, 'email': user.email}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


# Update user by user ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.json
        user.id = user_id
        user.full_name = data.get('full_name', user.full_name)
        user.email = data.get('email', user.email)
        user.services = data.get('services', user.services)
        try:
            db.session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error message': 'User not found'}), 404


# Delete user by user ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        try:
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'User not found'}), 404
