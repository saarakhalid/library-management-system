## Library Management System
# Introduction
This project is a library management system that manages relationships between books, authors, and members.

#  Tree
csharp
.
├── lib
│   ├── alembic.ini
│   ├── cli.py
│   ├── library.db
│   ├── helpers.py
│   ├── migrations
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 09dd296c9b65_created_all_my_tables_and_their_.py
│   ├── models.py
│   ├── seed.py
│   └── _pycache_
├── Pipfile
├── Pipfile.lock
└── README.md
# models.py
Contains classes for Book, Author, and Member.
Defines tables for books, authors, and members.
# seed.py
Populates the tables with data using Faker.
# cli.py
Command-line interface for interacting with the library management system.
Allows users to perform operations such as listing books, creating, updating, and deleting books, listing authors, creating, updating, and deleting authors, listing members, creating, updating, and deleting members, and exiting the program.
# helpers.py
Contains helper functions used in the library management system.
Includes functions for listing books, creating, updating, and deleting books, listing authors, creating, updating, and deleting authors, listing members, creating, updating, and deleting members.
# library.db
SQLite database file storing data for the library management system.
Contains tables for books, authors, and members.
# Technologies Used
Programming Language: Python
Libraries and Frameworks: SQLAlchemy, Faker
Database: SQLite
Dependency Management: Pipenv
# Features
Users can add new books by providing title, author, and other details.
Display a list of all books stored in the database.
Allow users to update the details of existing books, such as title, author, and other attributes.
Users can delete books, removing them from the system.
Users can add new authors by providing their details.
Display a list of all authors stored in the database.
Allow users to update the details of existing authors.
Users can delete authors, removing them from the system.
Users can add new members by providing their details.
Display a list of all members stored in the database.
Allow users to update the details of existing members.
Users can delete members, removing them from the system.