from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello!"


@app.route('/index')
def q():
    return "ewrwrwrrw"


@app.route('/index/<int:x>')
def index(x):
    return str(x + 2)


if __name__ == '__main__':
    app.run()
