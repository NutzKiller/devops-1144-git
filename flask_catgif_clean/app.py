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

# Fetch a random GIF from the database
def get_random_gif():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        connection.close()
        
        if result:
            return result['url']
        else:
            print("No URL found in database!")
            return None
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

@app.route('/')
def index():
    gif_url = get_random_gif()  # Fetch a random GIF URL
    return render_template('index.html', gif_url=gif_url)

@app.route('/new_gif')
def new_gif():
    gif_url = get_random_gif()  # Fetch another random GIF
    return jsonify({'new_gif_url': gif_url})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)