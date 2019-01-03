from flask import Flask
app = Flask(__name__)

#print(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "<h1>Dojo</h1>"
@app.route('/say/<name>')
def sayhi(name):
    return "<h1>Hi</h1>" + name
@app.route('/say/<name>')
def sayhi1(name):
    return "<h1>Hi</h1>" + name
@app.route('/say/<name>')
def sayhi2(name):
    return "<h1>Hi</h1>" + name
#@app.route('/repeat/<num>/<hello>')
#def repeat1(num):
#    return  hello*int(num)
#@app.route('repeat/99/dogs')
#def repeat2(num):
#    return "dogs"*int(num)
@app.route("/repeat/<number>/hello")
def hello(number): 
    print_statement = ""
    for i in range(0,int(number)): 
        print_statement = print_statement + "<p>hello</h3><p>"
        print("hello")
    return print_statement

@app.route("/repeat/<number>/dogs")
def dogs(number): 
    print_statement = ""
    for i in range(0,int(number)): 
        print_statement = print_statement + "<h1>dogs</h1>"
        print("dogs")
    return print_statement


if __name__=="__main__":
    
    app.run(debug=True) 