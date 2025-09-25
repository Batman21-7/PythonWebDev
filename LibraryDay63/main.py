from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    all_books = [{'id': book.id-1, 'title': book.title, 'author': book.author, 'rating': book.rating} for book in all_books]


@app.route('/')
def home():
    with app.app_context():
        global all_books, result
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars()
        all_books = [{'id': book.id-1, 'title': book.title, 'author': book.author, 'rating': book.rating} for book in all_books]
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        with app.app_context():
            new_book = Books(title=data['title'].title(), author=data['author'].title(), rating=data['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        with app.app_context():
            id = request.args.get('id', type=int) + 1
            new_book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
            new_book.rating = request.form['rating']
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', books=all_books, id=request.args.get('id', type=int))


@app.route('/delete')
def delete():
    with app.app_context():
        id = request.args.get('id', type=int) + 1
        print(id)
        print(type(id))
        book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
