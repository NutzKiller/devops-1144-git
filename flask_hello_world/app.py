from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/about')
def about():
    return "This is a simple Flask web app that greets users."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

