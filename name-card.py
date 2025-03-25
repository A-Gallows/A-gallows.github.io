from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
