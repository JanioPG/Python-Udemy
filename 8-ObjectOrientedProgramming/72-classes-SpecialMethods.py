# Métodos especiais: __str__, __len__, __del__

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book object has been deleted')
    

my_book = Book('Aventuras do Tony Bento', 'Nina Maria', 230)
print(my_book)
print(len(my_book))
del my_book
