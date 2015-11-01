from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    strr = '<h1>Test Safe</h1>'
    return render_template('user.html', name=name, strr=strr)


if __name__ == '__main__':
    app.run()
