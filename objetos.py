#Programacion orientada a objetos con clases. Booleanos. Metodos con funciones, append y remove. Uso de parametros, __init__ y self.

class Book:
    
    def __init__(self,title,author):
        self.title= title
        self.author= author
        self.available= True

    def borrow(self):

        if self.available:
            self.available = False
            print(f'El libro{self.title} ha sido prestado')
        else:
            print(f'El libro{self.title} no esta disponible')

    def return_book(self):
        self.available = True
        print(f'El libro{self.title} ha sido devuelto')

class User:
    
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=[]

    def borrow_boobks(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro{book.title} no esta disponible')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro{book.title} no esta en la lista de prestados') 

class Library:
    
    def __init__(self):
        self.books = []
        self.user = []
    
    def add_books(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado')

    def register_user(self,user):
        self.user.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def show_available_books(self):
        print('Libros disponibles:')

        for book in self.books:
            if book.available:
                print(f'{book.title}por{book.author}')

# Crear objetos 
#clase libro

book1= Book(' El vuelco del destino','Winston S. Churchill')
book2= Book(' El arte de la guerra','Sun Tzu')

# Crear usuario

user1= User(' Mariano' ,'Marito95')
user2= User(' Carla' ,'Cali82')

#Crear biblioteca

Library=Library()
Library.add_books(book1)
Library.add_books(book2)
Library.register_user(user1)
Library.register_user(user2)

#Llamando a las funciones

#Libros disponibles
Library.show_available_books()
#Libro prestado a un usuario
user1.borrow_boobks(book1)
#Libros disponibles
Library.show_available_books()
#Devolver libro
user1.return_book(book1)
Library.show_available_books()

