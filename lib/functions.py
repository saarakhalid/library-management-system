from seed import session
# from sqlalchemy import create_engine
from models import Book, Author, Member


def list_books():
    print("Listing all books:")
    books = session.query(Book).all()
    for book in books:
        print(book)

def find_book_by_title():
    title = input("Enter the title of the book:")
    book = session.query(Book).filter_by(title=title).first()
    print(
        "TITLE: ", book.title,
        "AUTHOR: ", book.author_name,
        "MEMBER ID: ", book.member_id
    )

def find_book_by_id():
    book_id = input("Enter the ID of the book:")
    book = session.query(Book).filter_by(id=book_id).first()
    print(
        "ID: ", book.id,
        "TITLE: ", book.title,
        "AUTHOR: ", book.author_name,
        "MEMBER ID: ", book.member_id
    )

def create_new_book():
    title = input("Enter the title of the book: ")
    author_name = input("Enter the name of the author: ")
    member_id = input("Enter the member ID who borrowed this book (leave empty if not borrowed): ")

    new_book = Book(title=title, author_name=author_name, member_id=member_id)

    session.add(new_book)
    session.commit()
    print(f"The new book '{title}' has been added successfully.")

def return_book():
    book_id = input("Enter the ID of the book to return: ")
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.member_id = None
        session.commit()
        print(f"The book '{book.title}' has been returned successfully.")
    else:
        print("Error: Book not found.")

def list_authors():
    print("Listing all authors:")
    authors = session.query(Author).all()
    for author in authors:
        print(author)

def find_author_by_name():
    name = input("Enter the name of the author:")
    author = session.query(Author).filter_by(name=name).first()
    print(
        "NAME: ", author.name,
        "BOOKS: ", [book.title for book in author.books]
    )

def find_author_by_id():
    author_id = input("Enter the ID of the author:")
    author = session.query(Author).filter_by(id=author_id).first()
    print(
        "ID: ", author.id,
        "NAME: ", author.name,
        "BOOKS: ", [book.title for book in author.books]
    )

def create_new_author():
    name = input("Enter the name of the author: ")

    new_author = Author(name=name)

    session.add(new_author)
    session.commit()
    print(f"The new author '{name}' has been added successfully.")

def delete_author():
    author_id = input("Enter the ID of the author to delete: ")
    author = session.query(Author).filter_by(id=author_id).first()
    if author:
        session.delete(author)
        session.commit()
        print(f"The author '{author.name}' has been deleted successfully.")
    else:
        print("Error: Author not found.")

def list_members():
    print("Listing all members:")
    members = session.query(Member).all()
    for member in members:
        print(member)

def find_member_by_name():
    name = input("Enter the name of the member:")
    member = session.query(Member).filter_by(name=name).first()
    print(
        "NAME: ", member.name,
        "BOOKS BORROWED: ", [book.title for book in member.books]
    )

def find_member_by_id():
    member_id = input("Enter the ID of the member:")
    member = session.query(Member).filter_by(id=member_id).first()
    print(
        "ID: ", member.id,
        "NAME: ", member.name,
        "BOOKS BORROWED: ", [book.title for book in member.books]
    )

def create_new_member():
    name = input("Enter the name of the member: ")

    new_member = Member(name=name)

    session.add(new_member)
    session.commit()
    print(f"The new member '{name}' has been added successfully.")

def delete_member():
    member_id = input("Enter the ID of the member to delete: ")
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        session.delete(member)
        session.commit()
        print(f"The member '{member.name}' has been deleted successfully.")
    else:
        print("Error: Member not found.")

def create_genre_to_book():
    title = input("Enter the title of the book to add genre to: ")
    book = session.query(Book).filter_by(title=title).first()
    if book:
        genre = input("Enter the genre of the book: ")
        book.genre = genre
        session.commit()
        print(f"The genre '{genre}' has been added to the book '{title}' successfully.")
    else:
        print("Error: Book not found.")

def create_book():
    print("Enter book details:")
    title = input("Title: ")
    author_name = input("Author's name: ")
    member_name = input("Borrower's name: ")

    author = session.query(Author).filter_by(name=author_name).first()
    member = session.query(Member).filter_by(name=member_name).first()

    if author is None:
        print("Author not found.")
        return
    if member is None:
        print("Member not found.")
        return

    # new_book = Book(title=title, author=author, member=member)
    # session.add(new_book)
    # session.commit()
    # # print("Book created successfully.")

def list_all_books():
    """Display all books in the library."""
    books = session.query(Book).all()
    for book in books:
        print(f"{book.title} by {book.author.name}")

def list_all_authors():
    """Display all authors in the library."""
    authors = session.query(Author).all()
    for author in authors:
        print(author.name)

def list_all_members():
    """Display all members in the library."""
    members = session.query(Member).all()
    for member in members:
        print(member.name)

def search_book_by_title(title):
    """Search for a book by its title."""
    book = session.query(Book).filter(Book.title == title).first()
    if book:
        print(f"{book.title} by {book.author.name}")
    else:
        print("Book not found.")

def search_book_by_author(author_name):
    """Search for books by a specific author."""
    author = session.query(Author).filter(Author.name == author_name).first()
    if author:
        for book in author.books:
            print(f"{book.title}")
    else:
        print("Author not found.")

def search_books_borrowed_by_member(member_name):
    """Search for books borrowed by a specific member."""
    member = session.query(Member).filter(Member.name == member_name).first()
    if member:
        for book in member.books:
            print(f"{book.title}")
    else:
        print("Member not found.")


def exit_program():
    print("THANK YOU!!")
    exit()


