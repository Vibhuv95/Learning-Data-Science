from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Jack"
    language = "Python"
    luckynos = [1, 5, 76, 86, 99, 100]
    footer = "<p> Copyright 2025 </p> | All right reversed"
    return render_template("index.html", name=name, lang=language, lucky = luckynos, footer=footer)   

app.run(debug=True)