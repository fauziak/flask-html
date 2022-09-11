#i nstalling flask app 
# pip 3 install Flask 
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Hello-World.html')

@app.route('/fauzia')
def hello_fauzia():
    return render_template('fauzia.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)