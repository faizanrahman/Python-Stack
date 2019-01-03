from flask import Flask, render_template, request, redirect, session, flash
import random
import datetime
app = Flask(__name__)
#Set a secret key to use sessions.
app.secret_key='1234'



#Create a function to generate a random number

def randomNum(start, end):
    num = random.randint(start, end)
    return num

def earn_lose():
    earnOrLose = random.randint(1,2)
    if earnOrLose == 1:
        return True
    else:
        return False


@app.route('/')
def index():
    if 'reversed' in session:
        print(session['reversed'])
    else:
        session['reversed'] = []
    
    if 'color' in session:
        print(session['color'])
    else:
        session['color'] = 'green'
    if 'total' in session:
        print(session['total'])
    else:
        session['total'] = 0
        print(session['total'])
    if 'activity' in session:
        pass
    else:
        session['activity'] = []
    return render_template('index.html',total=session['total'],activity = session['reversed'], color = session['color'])

@app.route('/process_money', methods=['POST'])
def process():
    date = datetime.datetime.now()
    if request.form['building'] == 'farm':
        print('This input is from farm')
        randomNumFarm = randomNum(10,21)
        session['total']+=randomNumFarm
        activity = "Earned " + str(randomNumFarm) + " golds" + " from the farm" "                                                                                                          " + str(date)
        test = {'message':activity, 'color':'green'}
        session['activity'].append(test)
        print(activity)
        print(randomNumFarm)
    elif  request.form['building'] == 'cave':
        print('This input is from cave')
        randomNumCave = randomNum(5,11)
        session['total']+=randomNumCave
        activity = "Earned " + str(randomNumCave) + " golds" + " from the cave" "                                                                                                          " + str(date)
        test = {'message':activity, 'color':'green'}
        session['activity'].append(test)
        print(activity)
        print(randomNumCave)
    elif  request.form['building'] == 'house':
        print('This input is from house')
        randomNumHouse = randomNum(2,6)
        session['total']+=randomNumHouse
        activity = "Earned " + str(randomNumHouse) + " golds" + " from the house" "                                                                                                       " + str(date)
        test = {'message':activity, 'color':'green'}
        session['activity'].append(test)
        print(activity)
        print(randomNumHouse)
    elif  request.form['building'] == 'casino':
        randomNumCasino = randomNum(0,50)
        print('This input is from casino')
        if earn_lose() == True:
            session['total']+=randomNumCasino
            activity = "Earned " + str(randomNumCasino) + " golds" + " from the casino" "                                                                                             " + str(date)
            test = {'message':activity, 'color':'green'}        
        elif earn_lose() == False:
            session['total']-=randomNumCasino
            session['color'] = 'red'
            activity = "Lost " + str(randomNumCasino) + " golds" + " from the casino" "                                                                                             " + str(date)
            test = {'message':activity, 'color':'red'}
        session['activity'].append(test)
        #print(activity)
    #session['color'] = 'green'
    session['reversed'] = session['activity'][::-1]
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if request.form['building'] == 'reset':
        session.clear()
    
    
    
    
    
    
    
    
    
    
    
    #Random number for farm
    # session.clear()
    # if request.form['farm'] == 'farm':
    #     print('This input is from farm')
    #     randomNumFarm = random.randint(10,21)
    #     if 'randomNumFarm' in session:
    #         print(session['randomNumFarm'])
    #     else: 
    #         session['randomNumFarm'] = randomNumFarm
    #     print(session['randomNumFarm'])


    # #Random number for cave
    # session.clear()
    # if request.form['cave'] == 'cave':
    #     print('This input is from cave')
    #     randomNumCave = random.randint(5,11)
    #     if 'randomNumCave' in session:
    #         print(session['randomNumCave'])
    #     else: 
    #         session['randomNumCave'] = randomNumCave
    #     print(session['randomNumCave'])


    # #Random number for house
    # session.clear()
    # if request.form['house'] == 'house':
    #     print('This input is from house')
    #     randomNumHouse = random.randint(2,6)
    #     if 'randomNumHouse' in session:
    #         print(session['randomNumHouse'])
    #     else: 
    #         session['randomNumHouse'] = randomNumHouse
    #     print(session['randomNumHouse'])

    #Random number for Casino
    # session.clear()
    # if request.form['casino'] == 'casino':
    #     print('This input is from casino')
    #     randomNumCave = random.randint(,11)
    #     if 'randomNumCave' in session:
    #         print(session['randomNumCave'])
    #     else: 
    #         session['randomNumCave'] = randomNumCave
    #     print(session['randomNumCave'])
    return redirect('/')


















if __name__=="__main__":
    app.run(debug=True)