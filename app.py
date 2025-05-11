from flask import Flask, render_template, redirect, url_for, request, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'papernestbookstore'  # For flashing messages

DB_FILE = 'db.json'

# Initialize the database if it doesn't exist
def initialize_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({"orders": []}, f)

# Load the database
def load_db():
    initialize_db()
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# Save to database
def save_to_db(data):
    db = load_db()
    db["orders"].append(data)
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/redirect', methods=['POST'])
def redirect_category():
    category = request.form.get('category')
    user_name = request.form.get('user_name', '')
    
    if not user_name.strip():
        # If no name was provided, go back to homepage
        return redirect(url_for('homepage'))
    
    if category == "children":
        return redirect(url_for('children_books', user_name=user_name))
    elif category == "fiction":
        return redirect(url_for('fiction_books', user_name=user_name))
    elif category == "non-fiction":
        return redirect(url_for('non_fiction_books', user_name=user_name))
    elif category == "mystery":
        return redirect(url_for('mystery_books', user_name=user_name))
    elif category == "history":
        return redirect(url_for('history_books', user_name=user_name))
    else:
        return redirect(url_for('homepage'))

@app.route('/books/children')
def children_books():
    user_name = request.args.get('user_name', 'Guest')
    books = [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
        {"title": "Charlotte's Web", "author": "E.B. White"},
        {"title": "The Cat in the Hat", "author": "Dr. Seuss"},
        {"title": "Matilda", "author": "Roald Dahl"},
        {"title": "Where the Wild Things Are", "author": "Maurice Sendak"}
    ]

    return render_template('children.html', books=books, user_name=user_name)

@app.route('/books/fiction')
def fiction_books():
    user_name = request.args.get('user_name', 'Guest')
    books = [
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger"}
    ]

    return render_template('fiction.html', books=books, user_name=user_name)

@app.route('/books/non_fiction')
def non_fiction_books():
    user_name = request.args.get('user_name', 'Guest')
    books = [
        {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari"},
        {"title": "Educated", "author": "Tara Westover"},
        {"title": "Becoming", "author": "Michelle Obama"},
        {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot"},
        {"title": "Unbroken", "author": "Laura Hillenbrand"}
    ]
    return render_template('non-fiction.html', books=books, user_name=user_name)

@app.route('/books/mystery')
def mystery_books():
    user_name = request.args.get('user_name', 'Guest')
    books = [
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
        {"title": "Gone Girl", "author": "Gillian Flynn"},
        {"title": "The Da Vinci Code", "author": "Dan Brown"},
        {"title": "Big Little Lies", "author": "Liane Moriarty"},
        {"title": "In the Woods", "author": "Tana French"}
    ]
    return render_template('mystery.html', books=books, user_name=user_name)

@app.route('/books/history')
def history_books():
    user_name = request.args.get('user_name', 'Guest')
    books = [
        {"title": "The Diary of a Young Girl", "author": "Anne Frank"},
        {"title": "Team of Rivals", "author": "Doris Kearns Goodwin"},
        {"title": "The Wright Brothers", "author": "David McCullough"},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond"},
        {"title": "1776", "author": "David McCullough"}
    ]
    return render_template('history.html', books=books, user_name=user_name)

@app.route('/save_order', methods=['POST'])
def save_order():
    # Get form data
    user_name = request.form.get('user_name', 'Guest')
    category = request.form.get('category', 'unknown')
    
    # Extract book selections
    selected_books = []
    for i in range(100):  # Assuming no more than 100 books per category
        quantity_key = f'book_{i}'
        if quantity_key not in request.form:
            break
            
        quantity = int(request.form.get(quantity_key, 0))
        if quantity > 0:
            title = request.form.get(f'title_{i}')
            author = request.form.get(f'author_{i}')
            selected_books.append({
                "title": title,
                "author": author,
                "quantity": quantity
            })
    
    # Create order record
    if selected_books:
        order = {
            "user_name": user_name,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "books": selected_books
        }
        
        # Save to JSON file
        save_to_db(order)
        
        # Flash success message (optional)
        flash("Your book selection has been saved!")
    
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)