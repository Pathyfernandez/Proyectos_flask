from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    session['counter'] += 2
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect(url_for('index'))

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    increment = int(request.form['increment'])
    session['counter'] += increment
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
