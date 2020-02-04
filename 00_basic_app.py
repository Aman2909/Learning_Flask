from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello!"


@app.route('/qwer')
def q():
    return "From qwer!"


if __name__ == '__main__':
    app.run()
