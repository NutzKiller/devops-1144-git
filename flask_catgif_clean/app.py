from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration (Update credentials as per your setup)
DB_CONFIG = {
    'host': 'db',  # Docker Compose service name for MySQL
    'user': 'root',  # MySQL username
    'password': 'root_password',  # Root password for MySQL
    'database': 'catgifs'  # The database you're using
}

# Fetch a random GIF from the database
def get_random_gif():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT url FROM images ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        connection.close()
        
        print(f"Fetched URL: {result['url'] if result else 'No URL'}")  # Debug the fetched URL
        return result['url'] if result else None
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None


@app.route('/')
def index():
    gif_url = get_random_gif()  # Fetch a random GIF URL
    print(f"Gif URL: {gif_url}")  # Debug
    return render_template('index.html', gif_url=gif_url)

@app.route('/new_gif')
def new_gif():
    gif_url = get_random_gif()  # Fetch another random GIF
    return jsonify({'new_gif_url': gif_url})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
