from library import Book, DVD, Magazine, LibraryItem, ItemStatus


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


print("Book repr:")
print(repr(book))