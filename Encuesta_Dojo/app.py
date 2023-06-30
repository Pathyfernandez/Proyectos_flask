from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['gender'] = request.form['gender']
        session['interests'] = request.form.getlist('interests')
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    name = session.get('name')
    gender = session.get('gender')
    interests = session.get('interests')
    return render_template('result.html', name=name, gender=gender, interests=interests)

if __name__ == '__main__':
    app.run(debug=True)
