from flask import Flask, request
from flask_cors import CORS

application = Flask(__name__)

CORS(application)

@application.route('/pay')
def root():
    return "<p>ML API</p>"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)