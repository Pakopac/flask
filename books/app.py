from flask import Flask, render_template
from jinja2 import Template 
import json
app = Flask(__name__)

# json importation
books_file = "assets/books.json"
with open(books_file) as json_file:
    books_load = json.load(json_file)
books_dump = json.dumps(books_load)
books_json = json.loads(books_dump)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=["GET"])
def books():
    return render_template('books.html', books=books_json)

@app.route('/api/book/id/<id>')
def book_by_id(id):
    return render_template('book_by_id.html', books=books_json, id=id)

@app.route('/api/book/title/<title>')
def book_by_title(title):
    return render_template('book_by_title.html', books=books_json, title=title)

if __name__ == '__main__':
    app.run(debug=True)