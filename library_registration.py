
class LibraryItem:
#    all_items = []
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year
#        LibraryItem.all_items.append(self)

    def display_info(self):
        print(f"Title : {self.title}  Publication Year : {self.publication_year}")

class Book(LibraryItem):
    def __init__(self, title, publication_year, author):
        super().__init__(title, publication_year)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Yazar : {self.author}")

class Magazine(LibraryItem):
    def __init__(self, title, publication_year, issue):
        super().__init__(title, publication_year)
        self.issue = issue
    
    def display_info(self):
        super().display_info()
        print(f"Magazine Issue : {self.issue}")

class DigitalItem:
    def download(self):
        print(f"{self.title} loading...")

class Ebook(Book, DigitalItem):
    def __init__(self, title, publication_year, author, file_size):
        Book.__init__(self, title, publication_year, author)
        self.file_size = file_size

        def display_info(self):
            Book.display_info()
            print(f"Ebook size : {self.file_size} MB")

class Member :

    def __init__(self, name):
        self.name = name
        self.borrowed_items = []
        self.borrow_limit = 3  #Number of items that can be borrowed at the same time.

    def borrow_item(self, item):
        if len(self.borrowed_items) >= self.borrow_limit :
            print(f"{self.name} has borrowed {self.borrow_limit} books, cannot buy more.")
        else:
            self.borrowed_items.append(item)
            print(f"{self.name} hasn't borrowed the item called {item.title}.")

    def return_item(self, item):
        if  self.borrowed_items :
            self.borrowed_items.remove(item)
            print(f"{self.name} has returned the item {item.title}")
        else :
            print(f"{self.name} has not borrowed the item called {item.title}")

    def display_borrowed(self):
        if self.borrowed_items:
            print(f"Works borrowed by {self.name}")
            for item in self.borrowed_items:
                print(f"- {item.title}")
        else :
            print(f"There are no works borrowed by {self.name}.")

# TEST PHASE
print("\n-----Book Info-----")
kitap = Book("Sefiller", 1862, "Victor Hugo")
kitap.display_info()

print("\n-----Magazine Info-----")
dergi = Magazine("National Geographic", 2021, "Ocak")
dergi.display_info()

print("\n-----E-book Info-----")
ekitap = Ebook("Dijital Dönüşüm", 2020, "Ahmet Yılmaz", 5)
ekitap.display_info()
ekitap.download()

print("\n-----Member Operations-----")
uye = Member("Elif")
uye.borrow_item(kitap)
uye.borrow_item(dergi)
uye.borrow_item(ekitap)
uye.borrow_item(dergi)
uye.display_borrowed()
uye.return_item(kitap)
uye.display_borrowed()
 


    



