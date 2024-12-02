from flask import Flask, render_template
from bd_check_withschedule import check_birthdays

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route to check today's birthdays
@app.route('/check_today')
def check_today():
    birthdays = check_birthdays()
    return render_template('today.html', birthdays=birthdays)

if __name__ == '__main__':
    app.run(debug=True)
