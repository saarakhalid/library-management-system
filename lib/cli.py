# lib/cli.py

from functions import (
    exit_program,
    create_book,
    list_books,
    create_new_author,
    delete_author,
    list_authors,
    create_new_member,
    delete_member,
    list_members
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_books()
            input("Press enter to continue")
        elif choice == "2":
            create_book()
            input("Press enter to continue")
        elif choice == "3":
            list_authors()
            input("Press enter to continue")
        elif choice == "4":
            create_new_author()
            input("Press enter to continue")
        elif choice == "5":
            delete_author()
            input("Press enter to continue")
        elif choice == "6":
            list_members()
            input("Press enter to continue")
        elif choice == "7":
            create_new_member()
            input("Press enter to continue")
        elif choice == "8":
            delete_member()
            input("Press enter to continue")
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all books")
    print("2. create a new book")
    print("3. List all authors")
    print("4. create a new author")
    print("5. Delete an author")
    print("6. List all members")
    print("7. create a new member")
    print("8. Delete a member")

if __name__ == "__main__":
    main()
