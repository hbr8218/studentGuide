from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))

@app.route('/')
def index():
    return "This is webapp for students"

if __name__ == '__main__':
    app.run()