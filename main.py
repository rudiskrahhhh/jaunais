from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["rudis", "roberts", "janis"]
    return render_template("saraksts.html", vardi = saraksts)


if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")