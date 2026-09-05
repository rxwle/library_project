from library.library import Library
from library.library_menu import LibraryMenu
import sys

def main():
    library = Library()
    library_menu = LibraryMenu(library)
    library.add_book("978-1", "Core Kotlin", "JetBrains Team")
    library.add_book("978-2", "Effective Java", "Joshua Bloch")
    library.add_book("978-3", "Clean Architecture", "Robert Martin")

    library.add_user("1", "Алексей (Студент)", "e", "Student")
    library.add_user("2", "Профессор Петров", "f", "Faculty")
    library.add_user("3", "Дмитрий (Гость)", "b", "Guest")
    try:
        library_menu.run()
    except KeyboardInterrupt:
        print("Программа закрывается принудительно")
        sys.exit()

    except EOFError:
        print("Конец ввода")
        sys.exit()


if __name__ == "__main__":
    main()