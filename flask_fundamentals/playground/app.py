from flask import Flask, render_template

app = Flask(__name__)
# def test(x,color):
#     str=""
#     for i in range(0,int(x)):
#         str+='<div class="display"></div>'
#     d= [x, color]
#     return d 

@app.route('/')


def hello_world():
    return render_template('index.html')

@app.route('/play')
def boxDisplay():    
    return render_template('index1.html')

@app.route('/play/<x>')
def numOfDisplay(x):
    str=""
    for i in range(0,int(x)):
        str+='<div class="display"></div>'
    return render_template('index1.html',context=str)

# color
@app.route('/play/<x>/<color>')
def bgred(x,color):
    str=""
    for i in range(0,int(x)):
        str+='<div class="display"></div>'
    return render_template('index1.html',color=color,context=str)

@app.route('/play/<x>/<color>/<width>')
def ext(x,color,width):
    str=""
    for i in range(0,int(x)):
        str+='<div class="display"></div>'
    return render_template('index1.html',color=color,context=str,width=width) 


    
#@app.route('/play/<y>/<color>')
#def colorOfDisplay(<y>,<color>):
#    return render_template('index1.html')

#@app.route("/repeat/<number>/hello")
#def hello(number): 
#    print_statement = ""
#    for i in range(0,int(number)): 
#        print_statement = print_statement + "<p>hello</h3><p>"
#        print("hello")
#    return print_statement

if __name__=="__main__":
    app.run(debug=True)

