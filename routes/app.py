from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!"

@app.route("/hola")
def hola():
    return "Hola!"

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)

@app.route("/default")
@app.route("/default/<string:dft>")
def default(dft="Texto Default"):
    return dft

if __name__ == "__main__":
    app.run(debug=True)
