from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    #qty = int(request.form['strawberries'])
    qtyS = request.form.get('strawberries', type=int)
    qtyB = request.form.get('bananas',type=int)
    qtyA = request.form.get('apples',type=int)
    qtyM = request.form.get('mangoes',type=int)
    total = str(int(request.form['strawberries']) + int(request.form['bananas']) + int(request.form['apples']) + int(request.form['mangoes']))

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    
    #str(qty)
    #print(request.form)
    #print(qty)
    #print(int(request.form['strawberries']))
    #print(int(request.form['bananas']))
    #print(int(request.form['apples']))
    #print(int(request.form['mangoes']))
    
    return render_template('checkout.html',qtyS=qtyS,qtyB=qtyB,qtyA=qtyA,qtyM=qtyM,total=total, first_name=first_name, last_name=last_name, student_id=student_id)

# @app.route('/fruits')
# def fruits():
#     return render_template('fruits.html')

if __name__=="__main__":
    app.run(debug=True)