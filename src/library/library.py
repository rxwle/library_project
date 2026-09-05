from book.book import Book
from users.users import Student, Faculty, Guest
from users.base_user import User
from factory.users_factory import UsersFactory
from borrow_notes.borrow_note import BorrowNote

class Library():
    """Класс библиотеки"""
    def __init__(self):
        self.all_books = {}
        self.users = {}
        self.borrow_history = []

    def add_book(self, title: str, author: str, isbn: str):
        """Добавить книгу в библиотеку"""
        if isbn in self.all_books:
            print("Такая книга уже существует")
            return
        if not title or not author or not isbn:
            print("Не все поля заполнены")
            return
        try:
            book = Book(title, author, isbn)
            self.all_books[isbn] = book
        except Exception as e:
            print(f"Не удалось добавить книгу:{e}")

    def remove_book(self, isbn:str):
        if isbn in self.all_books:
            if not (self.all_books[isbn].available_status):
                print("Нельзя удалить книгу, она у пользователя")
                return False
            del self.all_books[isbn]
            print("Книга успешно удалена")
            return True
        else:
            print("Такой книги не существет")
            return False

    def find_book(self, isbn: str):
        if not isbn in self.all_books:
            print("Книга не найдена")
            return None
        print("Книга найдена")
        return self.all_books[isbn]
    
    def search_books(self, search:str):
        res = []
        for book in self.all_books.values():
            if search in book.title or search in book.author or search in book.isbn:
                res.append(book)
        return res

    def add_user(self, name: str, id: int, email: str, role: str):
        """Добавить пользователя в систему"""
        if id in self.users:
            print("Пользователь с таким id уже существует")
            return
        if not name or not id or not email or not role:
            print("Не все поля заполнены")
            return
        try:
            user = UsersFactory.user_create(name, id, email, role)
            self.users[id] = user
        except Exception as e:
            print(f"Не удалось добавить пользователя:{e}")

    def find_user(self, id: int):
        if not id in self.users:
            print(f"Пользователь с id: {id} не найден")
            return None
        print("Пользователь найден")
        return self.users[id]
    
    def borrow_book(self, id: int, isbn: str):
        if not id in self.users or not isbn in self.all_books:
            print("Пользователь или книга не найдены")
            return False
        user = self.users[id]
        book = self.all_books[isbn]
        if not(user.can_get_books()):
            print("Пользователь превысил лимит взятых книг")
            return False
        if not(book.available_status):
            print("Книгу уже взяли")
            return False
        user.borrowedbooks.append(book)
        book.available_status = False
        record = BorrowNote(user, book)
        self.borrow_history.append(record)
        print("Книга успешно выдана")
        return True

    def return_book(self, id: int, isbn: str):
        if not id in self.users or not isbn in self.all_books:
            print("Пользователь или книга не найдены")
            return False
        user = self.users[id]
        book = self.all_books[isbn]

        user.borrowedbooks.remove(book)
        book.available_status = True