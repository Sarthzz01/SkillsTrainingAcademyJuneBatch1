from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps Students!"

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/userDetails")
def userDetails():
    return {"name" : "Sarthak Kane", "age" : "19", "maritalStatus" : "Not Married"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

