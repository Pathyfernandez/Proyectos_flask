from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['dojo_location'] = request.form['dojo_location']
        session['favorite_language'] = request.form['favorite_language']
        session['comment'] = request.form['comment']
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    name = session.get('name')
    country = session.get('dojo_location')
    favorite_language = session.get('favorite_language')
    comment = session.get('comment')
    return render_template('result.html', name=name, dojo_location=country, favorite_language=favorite_language, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
