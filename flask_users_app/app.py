from flask import Flask, jsonify

app = Flask(__name__)

users = []


@app.route("/users")
def get_users():
    """Return all users."""
    return jsonify({"users": users})


@app.route("/users/add/<name>")
def add_user(name: str):
    """Add a new user."""
    users.append(name)
    return jsonify({"name": name})


if __name__ == "__main__":
    app.run(debug=True)
