from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Visitor counter logic
visitor_count = 0

@app.route('/')
def index():
    global visitor_count
    return render_template('index.html', visitor_count=visitor_count)

@app.route('/reset_count')
def reset_count():
    global visitor_count
    visitor_count = 0  # Reset the count
    return redirect(url_for('index'))

# Linux routes
@app.route('/topics/linux')
def linux_index():
    return render_template('topics/linux/index.html')

@app.route('/topics/linux/learning')
def linux_learning():
    return render_template('topics/linux/learning.html')

@app.route('/topics/linux/questions')
def linux_questions():
    return render_template('topics/linux/questions.html')

@app.route('/topics/linux/test')
def linux_test():
    return render_template('topics/linux/test.html')

# SQL routes
@app.route('/topics/sql')
def sql_index():
    return render_template('topics/sql/index.html')

@app.route('/topics/sql/learning')
def sql_learning():
    return render_template('topics/sql/learning.html')

@app.route('/topics/sql/questions')
def sql_questions():
    return render_template('topics/sql/questions.html')

@app.route('/topics/sql/test')
def sql_test():
    return render_template('topics/sql/test.html')

# Bash routes
@app.route('/topics/bash')
def bash_index():
    return render_template('topics/bash/index.html')

@app.route('/topics/bash/learning')
def bash_learning():
    return render_template('topics/bash/learning.html')

@app.route('/topics/bash/questions')
def bash_questions():
    return render_template('topics/bash/questions.html')

@app.route('/topics/bash/test')
def bash_test():
    return render_template('topics/bash/test.html')

# Python routes
@app.route('/topics/python')
def python_index():
    return render_template('topics/python/index.html')

@app.route('/topics/python/learning')
def python_learning():
    return render_template('topics/python/learning.html')

@app.route('/topics/python/questions')
def python_questions():
    return render_template('topics/python/questions.html')

@app.route('/topics/python/test')
def python_test():
    return render_template('topics/python/test.html')

# Git routes
@app.route('/topics/git')
def git_index():
    return render_template('topics/git/index.html')

@app.route('/topics/git/learning')
def git_learning():
    return render_template('topics/git/learning.html')

@app.route('/topics/git/questions')
def git_questions():
    return render_template('topics/git/questions.html')

@app.route('/topics/git/test')
def git_test():
    return render_template('topics/git/test.html')

# GitHub routes
@app.route('/topics/github')
def github_index():
    return render_template('topics/github/index.html')

@app.route('/topics/github/learning')
def github_learning():
    return render_template('topics/github/learning.html')

@app.route('/topics/github/questions')
def github_questions():
    return render_template('topics/github/questions.html')

@app.route('/topics/github/test')
def github_test():
    return render_template('topics/github/test.html')

# Docker routes
@app.route('/topics/docker')
def docker_index():
    return render_template('topics/docker/index.html')

@app.route('/topics/docker/learning')
def docker_learning():
    return render_template('topics/docker/learning.html')

@app.route('/topics/docker/questions')
def docker_questions():
    return render_template('topics/docker/questions.html')

@app.route('/topics/docker/test')
def docker_test():
    return render_template('topics/docker/test.html')

# Ansible routes
@app.route('/topics/ansible')
def ansible_index():
    return render_template('topics/ansible/index.html')

@app.route('/topics/ansible/learning')
def ansible_learning():
    return render_template('topics/ansible/learning.html')

@app.route('/topics/ansible/questions')
def ansible_questions():
    return render_template('topics/ansible/questions.html')

@app.route('/topics/ansible/test')
def ansible_test():
    return render_template('topics/ansible/test.html')

if __name__ == '__main__':
    app.run(debug=True)
