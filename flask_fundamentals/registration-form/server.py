from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='1234'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def validate():
    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank")
    elif(request.form['first_name'].isalpha() == False):
        flash("First Name cannot contain any numbers")
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank")
    elif(request.form['last_name'].isaplha() == False):
        flash("Last Name cannot contain any numbers")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['password']) < 1:
        flash("Password cannot be blank")
    elif len(request.form['password']) < 8:
        flash("Password should be more than 8 characters")
    if len(request.form['password_confirm']) < 1:
        flash("Password confirmation cannot be blank")
    if request.form['password'] != request.form['password_confirm']:
        flash("Password and password confirmation fields must match")
   
    return redirect('/')
    
























if __name__ =="__main__":
    app.run(debug=True)