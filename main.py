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

# @app.route('/users', methods=['POST'])
# def add_user():
#     """Insert a new customer into the database."""
#     data = request.json
#     print(data)  # Debugging line to check what is received

#     # Use default data if none provided
#     if not data or 'name' not in data or 'email' not in data or 'age' not in data:
#         data = {
#             "name": "abhi",
#             "email": "abhi@gmail.com.com",
#             "age": 25
#         }

#     name = data.get('name')
#     email = data.get('email')
#     age = data.get('age')

#     connection = create_connection()
#     if connection is None:
#         return jsonify({"error": "Database connection failed"}), 500

#     cursor = connection.cursor()
#     try:
#         cursor.execute("INSERT INTO customer (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
#         connection.commit()
#         return jsonify({"id": cursor.lastrowid}), 201  # Return the ID of the new customer
#     except Error as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         cursor.close()
#         connection.close()



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

@app.route('/users/2', methods=['PUT'])
def update_user(user_id):
    """Update a user's information."""
    data = request.get_json()
    
    name = data.get('Nehaaa')
    email = data.get('nehayy@example.com')
    
    if not name and not email:
        return jsonify({"error": "At least one field (name or email) is required to update."}), 400
    
    connection = create_connection()
    cursor = connection.cursor()
    
    updates = []
    if name:
        updates.append("name = kashyap")
    if email:
        updates.append("email =kashyap@gmail.com")
    
    query = f"UPDATE customer SET {', '.join(updates)} WHERE id = 2"
    params = [value for value in (name, email) if value is not None] + [user_id]
    
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

#for adding the sample users========>
# @app.route('/add_sample_users', methods=['POST'])
# def add_sample_users():
#     """Add sample users to the database."""
#     sample_users = [
#         ("Alice Smith", "alice@example.com"),
#         ("Bob Johnson", "bob@example.com"),
#         ("Charlie Brown", "charlie@example.com"),
#         ("Diana Prince", "diana@example.com"),
#         ("Ethan Hunt", "ethan@example.com")
#     ]
    
#     connection = create_connection()
#     cursor = connection.cursor()
    
#     try:
#         cursor.executemany("INSERT INTO customer (name, email) VALUES (%s, %s)", sample_users)
#         connection.commit()
#         return jsonify({"message": f"{cursor.rowcount} sample users added successfully."}), 201
#     except Error as e:
#         connection.rollback()
#         return jsonify({"error": str(e)}), 500
#     finally:
#         cursor.close()
#         connection.close()

# if __name__ == '__main__':
#     app.run(debug=True)




if __name__ == '__main__':
    app.run(debug=True)
