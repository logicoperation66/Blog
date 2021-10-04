from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.facebook.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Witaj, {user.name}</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Witaj, {name}!</h1>'

@app.route('/request/')
def request():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Twoją przeglądarką jest{user_agent}'

