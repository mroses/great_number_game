from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(0, 100)   
    if "result" not in session:
        result = "no guess"
    else:
        result = session['result']
    print result
    return render_template('index.html', result=result)

@app.route('/guess', methods=['POST'])
def guess():
    #print request.form
    guess = int(request.form['guess']) #specify its integer or else it will think the number input into the form is a string "5"
    num = session['num']
    print num
    if num > guess:
        session['result'] = "low"
    elif num < guess:
        session['result'] = "high"
    else:
        session["result"] = "num"
    print session['result']
    print guess
    return redirect('/')
@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)