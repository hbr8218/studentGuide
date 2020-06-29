from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    # print(os.environ['APP_SETTINGS'])
    # ,env=os.environ.get('APP_SETTINGS'), db=os.environ.get('DATABASE_URL')
    return render_template('home.html')

@app.route('/signin')
def signIn():
    return render_template('signin.html')

@app.route('/signup')
def signUp():
    return render_template('signup.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/contents')
def contents():
    return render_template('contents.html')

if __name__ == '__main__':
    app.run()