from flask import Flask, jsonify, Response, request
import json, db

app = Flask(__name__)
'''
user1 = {'name': 'FC', 'firstname': 'Fulvio', 'lastname': 'Corno'}
user2 = {'name': 'LDR', 'firstname': 'Luigi', 'lastname': 'De Russis'}
user3 = {'name': 'AMR', 'firstname': 'Alberto', 'lastname': 'Monge Roffarello'}
users = [user1, user2, user3]
 '''


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users')
def api_users():
    users=db.all_users()
    return jsonify(users)


@app.route('/users/<name>')
def api_user(name):
    users = db.all_users()
    user = [u for u in users if u['name'] == name]
    if len(user) == 1:
        return jsonify(user)
    else:
        response = jsonify({ 'message': "Invalid user "+name })
        response.status_code = 404
        return response


@app.route('/users', methods=['POST'])
def api_create_user():
    if request.headers['Content-Type'] == 'application/json':
        new_user = request.json
        users.append(new_user)
    else:
        response = jsonify({ 'message': "Invalid Request"})
        response.status_code = 404
        return response


if __name__ == '__main__':
    app.run()
