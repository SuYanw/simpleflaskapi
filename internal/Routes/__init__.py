from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/users", methods=['GET'])
def list_users():
    return jsonify({'id':'412','name':'Glaubert','age':'26'})

@app.route("/users", methods=['POST'])
def create_users():
    return jsonify({'id':'412','name':'Glaubert','age':'26'})
    