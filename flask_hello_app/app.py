from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a greeting message."""
    return jsonify(
        {"message": "Hello, World! Welcome to Flask backend."}
    )


if __name__ == "__main__":
    app.run(debug=True)
