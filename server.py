from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Dojo')
def say_dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say_hi(name):
    return f'Hi {name}'

@app.route('/repeat/<int:number>/<string:word>')
def repeat(number,word):
     return number * f'{word}\n'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

