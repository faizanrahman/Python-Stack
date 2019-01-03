from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    request.form['name']
    request.form['email']
    request.form['location']
    request.form['language']
    request.form['comments']
    return render_template('result.html')

@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We have redirected the user to '/'")
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)