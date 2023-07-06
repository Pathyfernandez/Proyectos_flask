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
    User.save(request.form)
    return redirect('/leer')

@app.route('/leer/<int:id>')
def show(id):
    user = User.get_by_id(id)
    return render_template("mostrar.html", usuario=user)

@app.route('/leer/<int:id>/editar')
def edit(id):
    user = User.get_by_id(id)
    return render_template("editar.html", usuario=user)

@app.route('/leer/<int:id>/actualizar', methods=['POST'])
def update(id):
    data = {
        'id': id,
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/leer/{id}')

@app.route('/leer/<int:id>/eliminar')
def delete(id):
    User.delete(id)
    return redirect('/leer')

if __name__ == "__main__":
    app.run(debug=True)
