from flask import Flask, render_template
import requests

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Joke route
@app.route('/joke')
def joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke_data = response.json()
        return render_template('joke.html', joke=f"Here's a new joke: {joke_data['setup']} - {joke_data['punchline']}")
    else:
        return "Oops! Couldn't fetch a joke.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

