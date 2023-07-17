from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'THis commit is just to test if my commits are being properly signed'


if __name__ == '__main__':
    app.run()
