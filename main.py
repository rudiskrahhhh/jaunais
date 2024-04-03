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
    kopejais_saraksts = [["rudis","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s"], ["roberts", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtv-3G97RDAt-sgNqxhaEB4f2SDwVxJaOq7JOY0D_7zA&s"], ["janis", "https://www.darzaabc.lv/public/assets/images/products/Agrimatco/kartupe%C4%BCi/kartupeli-monalisa-dzeltenie-seklas-kartupelu-stadamais-materials.jpg"], ["traktar", "https://lh6.googleusercontent.com/Bs8IK7AzA7HDKeel06gttMMDPDoPNzBQdxUTgoKnnFpWhw8tDn8OUWeaaOZeIDnuujmOiEhPBlbDbkjSHKZb-EWByLlqgJCmkF-V-cRau3hEyNqGD-uWqrXEXxnSpvgxj8300Al7"]]
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)



if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")