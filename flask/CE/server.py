from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<name>')
def say_hello(name):
    return f'¡Hola, {name}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    result = '\n'.join([word] * num)
    return result

@app.route('/<path:path>')
def handle_error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)

