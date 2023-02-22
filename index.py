from flask import Flask, render_template

app = Flask(__name__)
route = app.route

@route("/") 
def home(): return render_template("home.html")

@route("/contato")
def contato(): return "<h1>email: teste@gmail.com</h1>"

@route("/usuarios/<nome>")
def user(nome): return render_template("users.html",nome=nome)

if __name__=="__main__": app.run(debug=True)