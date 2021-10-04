from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Ten dokument zawiera plik cookie!</h1>')
    response.set_cookie('odpoweidz', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return f'<h1>Witaj, {name}!</h1>'

@app.route('/request/')
def request():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Twoją przeglądarką jest{user_agent}'

