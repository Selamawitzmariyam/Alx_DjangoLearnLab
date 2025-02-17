from bookshelf.models import Book
 book = Book.objects.filter(title="1984")    
 book.delete()
 books = Book.objects.all()
 print(list(books))
 #[]
 
 