from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='1234'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    print(request.form)
    # Do some validation here
    if len(request.form['name']) < 1:
        #display validation errors
        flash("Name must be provided.",'name')
    if len(request.form['comments']) < 1:
        flash("Comments must be provided.",'comments')
    elif len(request.form['comments']) > 120:
        flash("Comments cannot exceed 120 characters",'comments')

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect('/result')
    

@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We have redirected the user to '/'")
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)