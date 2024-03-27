from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# Create a base class for declarative class definitions
Base = declarative_base()

# Define Author class representing authors table in the database
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    
# Define one-to-many relationship with books table
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name},)>"

# Define Book class representing books table in the database
class Book(Base):
    __tablename__= "books"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), unique=True, nullable=False)
    genre = Column(String(), nullable=False)
    author_id = Column(Integer(), ForeignKey('authors.id'))
    member_id = Column(Integer(), ForeignKey('members.id'))

    author = relationship('Author', back_populates='books')
    borrower = relationship('Member', back_populates='borrowed_books')

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, genre={self.genre}, author_id={self.author_id}, member_id={self.member_id})>"

# Define Member class representing members table in the database
class Member(Base):
    __tablename__ = "members"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
 # Define many-to-many relationship with books table
    borrowed_books = relationship('Book', back_populates='borrower')

    def __repr__(self):
        return f"<Member(id={self.id}, name={self.name})>"

if __name__ == '__main__':
    # Create engine and connect to the database
    engine = create_engine('sqlite:///library.db')
    
    # Create all tables defined in Base
    Base.metadata.create_all(engine)
    
    # Create a sessionmaker bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

   