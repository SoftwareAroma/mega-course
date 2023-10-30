from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    home_page = render_template("home.html")
    return home_page


@app.route('/about/')
def about():
    about_page = render_template("about.html")
    return about_page


if __name__ == "__main__":
    app.run(debug=True)
