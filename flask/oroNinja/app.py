from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretkey'

def initialize_session():
    session['gold'] = 0
    session['activities'] = []

def add_activity(activity):
    session['activities'].insert(0, activity)

def process_gold(building):
    buildings = {
        'farm': {'min': 10, 'max': 20},
        'cave': {'min': 5, 'max': 10},
        'house': {'min': 2, 'max': 5},
        'casino': {'min': -50, 'max': 50}
    }

    gold = random.randint(buildings[building]['min'], buildings[building]['max'])
    session['gold'] += gold

    if gold >= 0:
        activity = f"Earned {gold} gold from the {building}!"
        color = 'green'
    else:
        activity = f"Entered a {building} and lost {-gold} gold... Ouch..."
        color = 'red'

    add_activity({'activity': activity, 'color': color})

@app.route('/')
def index():
    if 'gold' not in session:
        initialize_session()

    return render_template('index.html', activities=session['activities'], gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    process_gold(building)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
