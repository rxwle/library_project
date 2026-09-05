from library.library import Library
from book.book import Book
from users.users import Student, Faculty, Guest
from users.base_user import User
from factory.users_factory import UsersFactory
from borrow_notes.borrow_note import BorrowNote
from datetime import datetime
import sys

class LibraryMenu():
    def __init__(self, library: Library):
        self.library = library
    
    def show_menu(self):
        print("========= МЕНЮ =========")
        print("1. Добавить книгу")
        print("2. Добавить пользователя")
        print("3. Выдать книгу пользователю")
        print("4. Вернуть книгу")
        print("5. Найти книги по name, author, isbn")
        print("6. Показать просроченные книги")
        print("0. Выход")

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Выберите пункт: "))
                match choice:
                    case 0:
                        print("Выход...")
                        sys.exit()
                    case 1:
                        self.dialog_add_book()
                    case 2:
                        self.dialog_add_user()
                    case 3:
                        self.dialog_borrow_book()
                    case 4:
                        self.dialog_return_book()
                    case 5:
                        self.dialog_search_books()
                    case 6:
                        self.library.get_overdue_books()
                    case unknown_command:
                        print("Нет такого пункта")

            except KeyboardInterrupt:
                print("Программа закрывается принудительно")
                sys.exit()

            except EOFError:
                print("Конец ввода")
                sys.exit()
                
            except Exception as e:
                print(f"Ошибка: {e}")


    def dialog_add_book(self):
        try:
            title = input("Введите название книги: ")
            author = input("Напишите автора книги: ")
            isbn = input("Введите isbn книги: ")
            if self.library.add_book(title, author, isbn):
                print("Книга успешно добавлена")
            else:
                print("Ошибка добавления книги")
        except Exception as e:
            print(f"Ошибка: {e}")

    def dialog_add_user(self):
        try:
            name = input("Введите имя: ")
            id = int(input("Введите id: "))
            email = input("Введите email: ")
            role = input("Введите должность: ")
            if self.library.add_user(name, id, email, role):
                print("Пользователь успешно добавлен")
            else:
                print("Ошибка добавления пользователя")
        except Exception as e:
            print(f"Ошибка: {e}")

    def dialog_borrow_book(self):
        try:
            id = int(input("Напишите ваш id: "))
            isbn = input("Введите isbn книги: ")
            if self.library.borrow_book(id, isbn):
                print("Книга успешно выдана")
            else:
                print("Ошибка выдачи книги")
        except Exception as e:
            print(f"Ошибка: {e}")

    def dialog_return_book(self):
        try:
            id = int(input("Напишите ваш id: "))
            isbn = input("Введите isbn книги: ")
            if self.library.return_book(id, isbn):
                print("Книга успешно возвращена")
            else:
                print("Ошибка возврата книги")
        except Exception as e:
            print(f"Ошибка: {e}")

    def dialog_search_books(self):
        try:
            choice = int(input("По чему хотите искать книгу(1 - название, 2 - автор, 3 - isbn): "))
            if choice == 1:
                title = input("Введите название книги: ")
                res = self.library.search_books(title)
                if res:
                    print("Результаты поиска:")
                    print(*res)
                else:
                    print("Ошибка поиска")

            elif choice == 2:
                author = input("Введите автора книги: ")
                res = self.library.search_books(author)
                if res:
                    print("Результаты поиска:")
                    print(*res)
                else:
                    print("Ошибка поиска")
            
            elif choice == 3:
                isbn = input("Введите isbn книги: ")
                res = self.library.search_books(isbn)
                if res:
                    print("Результаты поиска:")
                    print(*res)
                else:
                    print("Ошибка поиска")

            else:
                print("Нет такого пункта")

        except Exception as e:
            print(f"Ошибка ввода: {e}")