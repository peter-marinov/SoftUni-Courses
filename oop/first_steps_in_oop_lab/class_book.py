class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.name} by {self.author} has {self.pages}'

b = Book('Harry Potter and Gof', 'J.K. Rowling', 500)

print(b)
print(str(b))
print(b.name)
print(b.author)
print(b.pages)