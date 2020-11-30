from flask import Flask, render_template
from jinja2 import Template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ma_route/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)