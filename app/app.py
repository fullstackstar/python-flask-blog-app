import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(
        host='localhost',
        port=port,
        threaded=True,
        debug=False
    )
