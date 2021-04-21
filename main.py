from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resume")
def resume():
    return render_template("/resume.html")


@app.route("/services")
def services():
    return render_template("/services.html")


@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")


if __name__ == "__main__":
    app.run(use_reloader=True)