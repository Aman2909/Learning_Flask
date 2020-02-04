from flask import Flask, render_template
import change_dict

app = Flask(__name__)

e = {'a': 2, 'b': 4}


@app.route('/')
def welcome():
    return render_template("dict.html", e=e)


@app.route('/alter')
def q():
    change_dict.alter(e)
    return render_template("dict.html", e=e)


if __name__ == '__main__':
    app.run(debug=True)
