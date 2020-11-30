from flask import Flask, render_template
from jinja2 import Template 
app = Flask(__name__)

book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/books', methods=["GET"])
def books():
    return render_template('books.html', book=book)

@app.route('/api/book/<id>')
def book_by_id(id):
    return render_template('book_by_id.html', book=book, id=id)

if __name__ == '__main__':
    app.run(debug=True)