from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def juego_numeros():
    if 'numero_secreto' not in session:
        session['numero_secreto'] = random.randint(1, 100)
        session['intentos'] = 0

    if request.method == 'POST':
        numero = int(request.form['numero'])
        session['intentos'] += 1

        if numero == session['numero_secreto']:
            mensaje = f"¡Felicitaciones! Adivinaste el número en {session['intentos']} intentos."
            session.pop('numero_secreto')
            session.pop('intentos')
            return render_template('resultado.html', mensaje=mensaje, color='green')
        elif session['intentos'] == 5:
            mensaje = "¡Tú pierdes! Agotaste tus 5 intentos. Inténtalo de nuevo."
            session.pop('numero_secreto')
            session.pop('intentos')
            return render_template('resultado.html', mensaje=mensaje, color='red')
        elif numero < session['numero_secreto']:
            mensaje = "Demasiado bajo. Intenta nuevamente."
            return render_template('resultado.html', mensaje=mensaje, color='blue')
        else:
            mensaje = "Demasiado alto. Intenta nuevamente."
            return render_template('resultado.html', mensaje=mensaje, color='blue')

    return render_template('adivinanza.html')

if __name__ == '__main__':
    app.run()
