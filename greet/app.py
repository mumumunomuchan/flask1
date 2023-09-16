from flask import Flask

app = Flask(__name__)

current_env = app.config.get("FLASK_ENV")
print(f"Running in {current_env} mode")

@app.route('/welcom')
def welcom():
    return "welcome"

@app.route('/welcome/home')
def home():
    return "welcome home"

@app.route('/welcome/back')
def back():
    return "welcome back"

