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
    return render_template('chat.html')

@app.route('/a')
def a():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()