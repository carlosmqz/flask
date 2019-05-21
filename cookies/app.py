from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/cookie/set')
def set_cookie():
   resp = make_response(render_template("index.html"))
   resp.set_cookie("username","carlosmqz")

   return resp

@app.route('/cookie/read')
def cookie_read():
   username = request.cookies.get("username", None)
   if username == None:
       return "The cookie does not exist."
   return username

if __name__ == '__main__':
    app.run(debug=True)