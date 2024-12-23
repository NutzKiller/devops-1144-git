import os
from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Read database configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),  # Defaults to 'localhost' if not set
    'user': os.getenv('DB_USER', 'root'),      # Defaults to 'root' if not set
    'password': os.getenv('DB_PASSWORD', 'root_password'),  # Defaults to 'root_password' if not set
    'database': os.getenv('DB_NAME', 'catgifs')  # Defaults to 'catgifs' if not set
}

# Increment the visitor counter
def increment_visitor_counter():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("UPDATE visitors SET count = count + 1 WHERE id = 1")
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")




# Get the current visitor count
def get_visitor_count():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT count FROM visitors WHERE id = 1")
        result = cursor.fetchone()
        connection.close()
        return result['count'] if result else 0
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return 0

# Fetch a random GIF from the database
def get_random_gif():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        connection.close()
        return result['url'] if result else None
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

@app.route('/')
def index():
    increment_visitor_counter()  # Increment the counter
    gif_url = get_random_gif()  # Fetch a random GIF URL
    visitor_count = get_visitor_count()  # Get the total visitor count
    return render_template('index.html', gif_url=gif_url, visitor_count=visitor_count)

@app.route('/new_gif')
def new_gif():
    gif_url = get_random_gif()  # Fetch another random GIF
    return jsonify({'new_gif_url': gif_url})

@app.route('/visitor_count')
def visitor_count():
    count = get_visitor_count()  # Get the current visitor count
    return jsonify({'visitor_count': count})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
