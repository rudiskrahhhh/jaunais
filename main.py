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
    bildes = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgulzijmK-UbALHbYL6erchb80AOm3iQQnUXEKKgVtsQ&s", "https://i0.wp.com/boingboing.net/wp-content/uploads/2017/10/636432493977643917-michael-christopher-estes.jpg?fit=534%2C712&ssl=1", "https://i.natgeofe.com/k/ad9b542e-c4a0-4d0b-9147-da17121b4c98/MOmeow1_3x4.png"]
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes)


if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")