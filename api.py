from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "Welcome to My Flask Web Application!"

@app.route('/')
def index():
    return render_template('index.html')