from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Fetch a random meme
def get_random_meme():
    url = "https://dog.ceo/api/breeds/image/random"  # Using a stable dog API for simplicity
    response = requests.get(url)
    data = response.json()
    return data['message']  # Return the URL of the meme

@app.route('/')
def index():
    meme_url = get_random_meme()  # Get a random meme on page load
    return render_template('index.html', meme_url=meme_url)

@app.route('/new_meme')
def new_meme():
    meme_url = get_random_meme()  # Get a new meme
    return jsonify({'new_meme_url': meme_url})  # Return as JSON

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
