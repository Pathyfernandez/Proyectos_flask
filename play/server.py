from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/')
@app.route('/play/<int:x>/')
@app.route('/play/<int:x>/<color>')
def play(x=1, color='blue'):
    num_boxes = x
    return render_template('index.html', num_boxes=num_boxes, color=color)

if __name__ == '__main__':
    app.run()
