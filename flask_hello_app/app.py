from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Hello, World! Welcome to Flask backend."}

if __name__ == '__main__':
    app.run(debug=True)
