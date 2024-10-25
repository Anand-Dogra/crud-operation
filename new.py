from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

def create_connection():
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Anand@123',
            database='test_python'
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(users)
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": "Name and email are required."}), 400
    
    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO customer (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        user_id = cursor.lastrowid
        return jsonify({"id": user_id, "name": name, "email": email}), 201
    except Error as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's information."""
    data = request.get_json()
    
    name = data.get('name')  # Get name from JSON payload
    email = data.get('email')  # Get email from JSON payload
    
    if not name and not email:
        return jsonify({"error": "At least one field (name or email) is required to update."}), 400
    
    connection = create_connection()
    cursor = connection.cursor()
    
    updates = []
    params = []
    
    if name:
        updates.append("name = %s")
        params.append(name)
    if email:
        updates.append("email = %s")
        params.append(email)
    
    # Construct the query
    query = f"UPDATE customer SET {', '.join(updates)} WHERE id = %s"
    params.append(user_id)  # Add user_id to params
    
    try:
        cursor.execute(query, params)
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found."}), 404
        return jsonify({"message": "User updated successfully."}), 200
    except Error as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()
if __name__ == '__main__':
    app.run(debug=True)