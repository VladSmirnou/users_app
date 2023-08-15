from flask import Flask, request
from pymongo import MongoClient


app = Flask(__name__)


client = MongoClient('mongodb://mongo:27017/')
db = client['users_db']
collection = db['users']


@app.route('/api/v1/user', methods=['POST'])
def save_name():
    username = request.get_json().get('username')

    if username:
        collection.insert_one({'username': username})
        return {'message': 'user created successfully'}, 201
    return {'error': 'provide a name'}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
