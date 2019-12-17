import os
from flask import flask

app = flask(__name__)


@app.route('/')


def hello():
    return 'Hello world ...... again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)