from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
#Set a secret key to use sessions.
app.secret_key='1234'

@app.route('/')
def index():
    if 'count' in session:
        print('count')
    else:
        session['count'] = 0
    session['count']+=1
    return render_template('index.html', count=session['count'])

@app.route('/by2', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    #We only increment by 1 since reloading the page also increments
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)