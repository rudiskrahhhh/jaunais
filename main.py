

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "heyaa"

if __name__ =='__main__':
    app.run(port = 5000)

print("heyaa")
