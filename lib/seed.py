from models import create_engine, sessionmaker, Author, Book, Member
from faker import Faker
import random

# Create engine and session
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create Faker object
fake = Faker()

# Seed Authors
print("Seeding Authors")
authors = [Author(name=fake.name()) for _ in range(15)]
session.add_all(authors)
session.commit()

# Seed Members
print("Seeding Members")
members = [Member(name=fake.name()) for _ in range(15)]
session.add_all(members)
session.commit()

# Seed Books
print("Seeding Books")
genres = ["Fiction", "Non-fiction", "Romance", "Thriller", "Mystery", "Science Fiction", "Fantasy", "Horror"]

# Create 2 books for each author
for author in authors:
    for _ in range(2):
        book = Book(title=fake.catch_phrase(), genre=random.choice(genres), author=author, borrower=random.choice(members))
        session.add(book)

session.commit()

print("All data seeded successfully")
