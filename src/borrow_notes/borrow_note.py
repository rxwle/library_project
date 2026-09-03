from datetime import datetime

class BorrowNote():
    """Записи одолжения книг"""
    def __init__(self, back_day: int, user_id, book_isbn: str, borrow_date: datetime):
        self.back_day = back_day
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.borrow_date = borrow_date
        self.returned_day = None

    def is_overstayed(self):
        """Просрочено ли одолжение книги"""
        if self.returned_day:
            return False
        return self.back_day < datetime.now()