from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def redirect_homepage():
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/eth")
def eth():
    return render_template("ethereum.html")

@app.route("/btc")
def btc():
    return render_template("bitcoin.html")

@app.route("/sol")
def sol():
    return render_template("solana.html")

@app.route("/dogecoin")
def doge():
    return render_template("dogecoin.html")

if __name__ == "__main__":
    app.run(debug=True)