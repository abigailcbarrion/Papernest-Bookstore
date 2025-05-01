from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/redirect', methods=['POST'])
def redirect_category():
    category = request.form.get('category')
    if category == "children":
        return redirect(url_for('children_books'))
    elif category == "fiction":
        return redirect(url_for('fiction_books'))
    elif category == "non-fiction":
        return redirect(url_for('non_fiction_books'))
    elif category == "mystery":
        return redirect(url_for('mystery_books'))
    elif category == "history":
        return redirect(url_for('history_books'))
    else:
        return redirect(url_for('homepage'))

@app.route('/books/children')
def children_books():
    books = [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
        {"title": "Charlotte's Web", "author": "E.B. White"},
        {"title": "The Cat in the Hat", "author": "Dr. Seuss"},
        {"title": "Matilda", "author": "Roald Dahl"},
        {"title": "Where the Wild Things Are", "author": "Maurice Sendak"}
    ]

    return render_template('children.html', books=books)

@app.route('/books/fiction')
def fiction_books():
    books = [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
        {"title": "Charlotte's Web", "author": "E.B. White"},
        {"title": "The Cat in the Hat", "author": "Dr. Seuss"},
        {"title": "Matilda", "author": "Roald Dahl"},
        {"title": "Where the Wild Things Are", "author": "Maurice Sendak"}
    ]

    return render_template('fiction.html', books=books)

@app.route('/books/non_fiction')
def non_fiction_books():
    books = [
        {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari"},
        {"title": "Educated", "author": "Tara Westover"},
        {"title": "Becoming", "author": "Michelle Obama"},
        {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot"},
        {"title": "Unbroken", "author": "Laura Hillenbrand"}
    ]
    return render_template('non-fiction.html', books=books)

@app.route('/books/mystery')
def mystery_books():
    books = [
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
        {"title": "Gone Girl", "author": "Gillian Flynn"},
        {"title": "The Da Vinci Code", "author": "Dan Brown"},
        {"title": "Big Little Lies", "author": "Liane Moriarty"},
        {"title": "In the Woods", "author": "Tana French"}
    ]
    return render_template('mystery.html', books=books)

@app.route('/books/history')
def history_books():
    books = [
        {"title": "The Diary of a Young Girl", "author": "Anne Frank"},
        {"title": "Team of Rivals", "author": "Doris Kearns Goodwin"},
        {"title": "The Wright Brothers", "author": "David McCullough"},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond"},
        {"title": "1776", "author": "David McCullough"}
    ]
    return render_template('history.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)