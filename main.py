from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/request/')
def request():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Twoją przeglądarką jest{user_agent}'

