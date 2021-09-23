from flask import Flask

app = Flask(__name__)


@app.route('/foo')
def foo():
    return {'ready': 'ok'}


@app.route('/404')
def bar():
    return {'ready': 'not'}
