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
def add_user():
    """Insert a new customer into the database."""
    data = request.json
    print(data)  # Debugging line to check what is received

    # Use default data if none provided
    if not data or 'name' not in data or 'email' not in data or 'age' not in data:
        data = {
            "name": "abhi",
            "email": "abhi@gmail.com.com",
            "age": 25
        }

    name = data.get('name')
    email = data.get('email')
    age = data.get('age')

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO customer (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        connection.commit()
        return jsonify({"id": cursor.lastrowid}), 201  # Return the ID of the new customer
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()




# @app.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     """Update an existing customer."""
#     data = request.json
#     print(data)  # Debugging line to check what is received

#     # Manually defined default values for update
#     default_name = "Updated Name"
#     default_email = "updated@example.com"
#     default_age = 67

#     # If no data is received, use default values
#     if not data or 'name' not in data or 'email' not in data or 'age' not in data:
#         data = {
#             "name": default_name,
#             "email": default_email,
#             "age": default_age
#         }

#     name = data.get('name')
#     email = data.get('email')
#     age = data.get('age')

#     connection = create_connection()
#     if connection is None:
#         return jsonify({"error": "Database connection failed"}), 500

#     cursor = connection.cursor()
#     try:
#         # Prepare the update statement
#         query = "UPDATE customer SET name = %s, email = %s, age = %s WHERE id = %s"
#         cursor.execute(query, (name, email, age, id))
#         connection.commit()

#         if cursor.rowcount == 0:
#             return jsonify({"error": "Customer not found"}), 404

#         return jsonify({"message": "Customer updated successfully"}), 200
#     except Error as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         cursor.close()
#         connection.close()


if __name__ == '__main__':
    app.run(debug=True)