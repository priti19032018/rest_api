from flask import Flask, jsonify, request, abort, url_for

app = Flask(__name__)

# In-memory store: mapping id -> user dict
users = {}
_next_id = 1

def _get_next_id():
    global _next_id
    val = _next_id
    _next_id += 1
    return val

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

# GET /users  -> list all users
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(list(users.values())), 200

# GET /users/<id> -> single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404)
    return jsonify(user), 200

# POST /users -> create user
@app.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        abort(400)
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    # basic validation
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    user_id = _get_next_id()
    user = {"id": user_id, "name": name, "email": email}
    users[user_id] = user

    resp = jsonify(user)
    resp.status_code = 201
    resp.headers['Location'] = url_for('get_user', user_id=user_id)
    return resp

# PUT /users/<id> -> update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.is_json:
        abort(400)
    user = users.get(user_id)
    if not user:
        abort(404)

    data = request.get_json()
    # update only provided fields
    name = data.get('name', user['name'])
    email = data.get('email', user['email'])
    user.update({"name": name, "email": email})
    return jsonify(user), 200

# DELETE /users/<id> -> delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, port=5000)
