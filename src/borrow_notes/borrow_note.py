from datetime import datetime, timedelta
from book.book import Book
from users.base_user import User

class BorrowNote():
    """Записи одолжения книг"""
    def __init__(self, user: User, book: Book):
        self.user_id = user.id
        self.book_isbn = book.book_isbn
        self.borrow_date = datetime.now()
        self.back_day = self.borrow_date + timedelta(days=user.get_borrow_days())
        self.returned_day = None

    def is_overstayed(self):
        """Просрочено ли одолжение книги"""
        if self.returned_day:
            return False
        return self.back_day < datetime.now()