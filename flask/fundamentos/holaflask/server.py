from flask import Flask

app = Flask(__name__)

@app.route ('/bienvenidas', methods = ['GET'])
def mensaje_bienvenida():
    return 'Bienvenidas al Mundo de Flask'

@app.route("/prueba", methods=['GET']) 
def prueba():
    return "Esto es la segunda ruta"

@app.route("/multiplica/<int:num1>", methods=['GET'])
def multiplica_por_diez(num1):
    total = num1 * 10
    return f"El resultado de multiplicar {num1} por 10 es {total}"

@app.route("/multiplica/<int:num1>/<int:num2>", methods=['GET'])
def multiplica_dos_numeros(num1, num2):
    total = num1 * num2
    return f"El resultado de multiplicar {num1} x {num2} es {total}"



if __name__ == '__main__':
    app.run(debug=True)

