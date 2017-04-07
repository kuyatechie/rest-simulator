from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/http-secured")
def hello():
    return "Successfully accessed secured HTTP!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)