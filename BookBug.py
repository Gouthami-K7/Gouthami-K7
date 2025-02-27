import os

# Function to create directories (books and transactions)
def create_directories():
    os.makedirs("LibraryManagementSystem/books", exist_ok=True)
    os.makedirs("LibraryManagementSystem/transactions", exist_ok=True)

# Function to add a book
def add_book(book_id, title, author, isbn, year):
    book_data = f"Title: {title}\nAuthor: {author}\nISBN: {isbn}\nYear: {year}\nStatus: Available"
    with open(f"LibraryManagementSystem/books/{book_id}.txt", 'w') as book_file:
        book_file.write(book_data)

# Function to search a book by title and check availability
def search_book(title):
    book_found = False

    # Iterate through the books directory to search for the book
    for book_file in os.listdir("LibraryManagementSystem/books"):
        if book_file.endswith(".txt"):
            with open(f"LibraryManagementSystem/books/{book_file}", 'r') as file:
                book_data = file.read()
                # Check if the title is mentioned in the book data
                if f"Title: {title}" in book_data:
                    book_found = True
                    # Check availability status
                    if "Status: Available" in book_data:
                            print("Pay to borrow book!!")
                    if "Status: Available" in book_data:
                        return f"Book Found: \n{book_data}\nBook Status: Available"
                        
                            
                    else:
                        return f"Book Found: \n{book_data}\nBook Status: Not Available"

    if not book_found:
        return "Book not found."

# Function to borrow a book
def borrow_book(book_id, member_name):
    book_path = f"LibraryManagementSystem/books/{book_id}.txt"
    
    # Check if book exists and is available
    if os.path.exists(book_path):
        with open(book_path, 'r+') as book_file:
            book_data = book_file.read()
            if "Status: Available" in book_data:
                # Change the status to borrowed
                book_data = book_data.replace("Status: Available", "Status: Borrowed")
                book_file.seek(0)
                book_file.write(book_data)

                # Log the transaction
                transaction_data = f"Transaction: Borrow\nBook ID: {book_id}\nMember: {member_name}\nStatus: Borrowed"
                transaction_file_name = f"LibraryManagementSystem/transactions/transaction_{book_id}.txt"
                with open(transaction_file_name, 'w') as transaction_file:
                    transaction_file.write(transaction_data)
                
                    
                return f"The book '{book_id}' has been borrowed by {member_name}."
            else:
                return "This book is currently not available."
    else:
        return "Book not found."

# Main function to demonstrate the workflow
def main():
    create_directories()  # Create necessary directories

    # Add some books
    add_book("book1", "MY FAULT", "Bindu", "83321", "2023")
    add_book("book2", "IKIGAI", "Devi", "927313", "2017")
    add_book("book3", "Charle and Choclate Factory", "Gouthami", "42192", "2013")

    # Search for a book
    print(search_book("MY FAULT"))
    print(search_book("IKIGAI"))
    print(search_book("Charle and Choclate Factory"))

    # Borrow a book
    print(borrow_book("book1", "Bindu"))
    print(borrow_book("book2", "Devi"))

    # Check again after borrowing
    print(search_book("MY FAULT"))

if __name__ == "__main__":
    main()