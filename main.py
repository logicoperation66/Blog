from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.facebook.com')

@app.route('/user/<name>')
def user(name):
    return f'<h1>Witaj, {name}!</h1>'

@app.route('/request/')
def request():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Twoją przeglądarką jest{user_agent}'

