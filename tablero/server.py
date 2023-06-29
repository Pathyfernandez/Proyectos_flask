from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chessboard():
    return render_template('index.html', rows=8, cols=8)

@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
def custom_chessboard(x=8, y=8):
    return render_template('index.html', rows=x, cols=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colored_chessboard(x=8, y=8, color1='white', color2='black'):
    return render_template('index.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
