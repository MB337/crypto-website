from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def redirect_homepage():
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)