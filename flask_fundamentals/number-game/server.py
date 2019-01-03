from flask import Flask, render_template, request, redirect, session, flash
import random
app=Flask(__name__)
app.secret_key='1234'

@app.route('/',methods=['GET','POST'])
def index():
    # Each time a page reloads, clear session data.
    session.clear()
    randomNum = random.randint(1,101)
    if 'randomNum' in session:
        print(session['randomNum'])
    else:
        session['randomNum'] = randomNum
    print(session['randomNum'])
    return render_template('index.html')

@app.route('/guess', methods=['GET','POST'])
def guess():
    if 'guess' in session:
        print('guess')
    else:
        session['guess'] = request.form['user-guess']
    
    if int(session['guess']) < session['randomNum']:
        print("This is too low")    
        message = "This is too low"
    elif int(session['guess']) == session['randomNum']:
        print("That's it. YOU GOT IT")
        message = "That's it. YOU GOT IT."
        color = 'green'
    else:
        print("This is too high")
        message = "This is too high"
    session.pop('guess')
    return render_template('index.html', message=message, color=color)

















if __name__=="__main__":
    app.run(debug=True)