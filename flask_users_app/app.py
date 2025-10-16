from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Sudha", "email": "sudha@example.com"},
    {"id": 2, "name": "Ravi", "email": "ravi@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == '__main__':
    app.run(debug=True)
