# import the Flask class from the flask module.
from flask import Flask
from flask_cors import CORS		# newly added


app = Flask(__name__)
CORS(app) #mitigate(reduce) CORS errors - a type of error related to making requests to domains other than the one that hosts this webpage.


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/bananas')
def bananas():
    return 'This page has bananas!'
    
@app.route('/bread')
def bread():
    return 'This page has bread!'







# this ensures that the server is only run if the script is executed directly, not when imported as a module
if __name__ == '__main__':
    app.run()