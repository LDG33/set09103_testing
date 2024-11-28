from flask import Flask 
app = Flask(__name__)

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
    return 'Goodbye'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)