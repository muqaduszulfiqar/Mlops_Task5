from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client['mydatabase']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        user = {'name': name, 'email': email}
        collection.insert_one(user)
        return jsonify({'message': 'User data stored successfully'}), 201
    else:
        return jsonify({'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
