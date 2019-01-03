from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    list = [
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1],
        [1,2,1,2,1,2,1,2],
        [2,1,2,1,2,1,2,1]
    ]
    str = ""
    for i in list:
        str+="<div>"
        for j in i:
            str += "<div class='box'"
            if j == 1:
                str+="style='background-color:red'"
            if j == 2:
                str+="style='background-color:black'"
            str+=">hello</div>"
        str+="</div>"
    return render_template("index.html",context=str)

@app.route('/<x>/<y>')
def newboard(x,y):
    rowNum = 0;
    str1 = ""
    for i in range(0,int(x)):
        str1+="<div>"
        if(rowNum%2 == 0):
            for j in range(0,int(y)):
                if(j % 2==0):
                    str1+="<div class='box-blue'>"+str(j)+"</div>"
                else:
                    str1+="<div class='box-red'>"+str(j)+"</div>"
        else:
            for j in range(1,int(y)+1):
                if(j % 2==0):
                    str1+="<div class='box-blue'>"+str(j)+"</div>"
                else:
                    str1+="<div class='box-red'>"+str(j)+"</div>"
        str1+="</div>"
        rowNum += 1;
    return render_template('index.html',str1=str1)




if __name__=="__main__":
    app.run(debug=True)
