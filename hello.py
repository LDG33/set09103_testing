from flask import Flask, redirect, url_for, session
app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/') 
def hello_world():
    return 'Hello Napier'

@app.route('/login') 
def login():
    return redirect(url_for('welcome'))

@app.route('/welcome/') 
def welcome():
    return 'Welcome'


@app.route('/goodbye/') 
def goodbye():
    try:
        if(session['imie']):
            return "The name %s provided in sessions was: %s" %(session['imie'],session['imie'])
    except KeyError:
        pass
    return "No sesion variable set for imie key"
    

@app.route('/good2/') 
def good():
    total=0
    for x in range(1,10200):
       total+=x
    return "<h1><i>Cool Stuff intiger: "+str(total)+"</i></h1>"

@app.route('/login2/<imie>') 
def login2(imie=None):
    session['imie']= imie
    #session.pop('imie', None)
    return redirect(url_for('goodbye'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)