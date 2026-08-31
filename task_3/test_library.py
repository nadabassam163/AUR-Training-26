from library import Book, DVD, Magazine, LibraryItem, Library



book = Book("Dune", "Frank Herbert", "9780441013593")
dvd = DVD("Inception", "Christopher Nolan")
magazine = Magazine("National Geographic", "2026-08")



print(book)
print(dvd)
print(magazine)



print("Book loan period:", book.loan_period)
print("DVD loan period:", dvd.loan_period)
print("Magazine loan period:", magazine.loan_period)



book.checkout()
print("After checkout:", book.status)

book.return_item()
print("After return:", book.status)



book.mark_lost()
print("After marking lost:", book.status)



print("ISBN valid:", LibraryItem.validate_isbn("9780441013593"))



items = [magazine, book, dvd]

print("Sorted items:")
for item in sorted(items):
    print(item)


# Test repr
print("Book repr:")
print(repr(book))




print("\n--- Library Tests ---")

library = Library()

# Use fresh items for Library tests
library_book = Book("Dune", "Frank Herbert", "9780441013593")
library_dvd = DVD("Inception", "Christopher Nolan")
library_magazine = Magazine("National Geographic", "2026-08")

library.add_item(library_book)
library.add_item(library_dvd)
library.add_item(library_magazine)



print("Found:", library.find_by_title("Dune"))



print("Available items:")

for item in library.list_available():
    print(item)



library.checkout_item("Dune")

print("After checkout:")

for item in library.list_available():
    print(item)



library.return_item("Dune")

print("After return:")

for item in library.list_available():
    print(item)

from database import Database


print("\n--- Database Tests ---")

database = Database("task_3/database.txt")

loaded_items = database.load()

print("Loaded items:")

for item in loaded_items:
    print(item)

database.save(loaded_items)

print("Database save completed.")