from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("serviceconnect-4d808-firebase-adminsdk-fbsvc-cd9e47e4d3.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firestore database object (THIS FIXES YOUR ERROR)
db = firestore.client()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/templates/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/providers")
def providers():
    providers_ref = db.collection("providers").stream()
    return jsonify([doc.to_dict() for doc in providers_ref])


if __name__ == "__main__":
    app.run(debug=True)
