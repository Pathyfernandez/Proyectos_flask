from flask import Flask, render_template, request, redirect
from leer import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/leer')

@app.route('/leer')
def users():
    return render_template("leer.html", usuarios=User.get_all())

@app.route('/leer/crear')
def new():
    return render_template("crear.html")

@app.route('/leer/crear', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/leer')

if __name__ == "__main__":
    app.run(debug=True)
