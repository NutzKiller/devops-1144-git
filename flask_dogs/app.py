from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
