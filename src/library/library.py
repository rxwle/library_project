from book.book import Book
from users.users import Student, Faculty, Guest
from users.base_user import User
from factory.users_factory import UsersFactory 

class Library():
    """Класс библиотеки"""
    def __init__(self):
        self.all_books = {}
        self.users = {}

    def _add_book(self, title, author, isbn):
        """Добавить книгу в библиотеку"""
        if isbn in self.all_books:
            print("Такая книга уже существует")
            return
        try:
            book = Book(title, author, isbn)
            self.all_books[isbn] = book
        except Exception as e:
            print(f"Не удалось добавить книгу:{e}")

    def _add_user(self, name: str, id: int, email: str, role: str):
        """Добавить пользователя в систему"""
        if id in self.users:
            print("Пользователь с таким id уже существует")
            return
        try:
            user = UsersFactory.user_create(name, id, email, role)
            self.users[id] = user
        except Exception as e:
            print(f"Не удалось добавить пользователя:{e}")

    