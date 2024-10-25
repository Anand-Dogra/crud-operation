import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',  # Replace with your MySQL username
            password='Anand@123',  # Replace with your MySQL password
            database='test_python'  # Update to your database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_customer(connection, name, email, age):
    """Create a new user."""
    query = "INSERT INTO customer (name, email, age) VALUES (%s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(query, (name, email, age))
    connection.commit()
    cursor.close()
    print("customer created successfully")

# # Example usage
if __name__ == "__main__":
    conn = create_connection()
if conn:  # Ensure the connection was successful
        # Adding the users
        customer = [
            ("Anand", "Anand@gmail.com", 24),
            ("Ashwani", "Ashwani@gmail.com", 25)
        ]
        
        for customer in customer:
            create_customer(conn, customer[0], customer[1], customer[2])
        conn.close()

       
    
#     if conn:  # Ensure the connection was successful
#         # Adding the users
#         users = [
#             ("Anand", "Anand@gmail.com", 24),
#             ("Ashwani", "Ashwani@gmail.com", 25)
#         ]
        
#         for user in users:
#             create_user(conn, user[0], user[1], user[2])
        
        # Close the connection when done
        # conn.close()
