from users.base_user import User

class Student(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email, max_borrowed_books=3, borrow_days=14)

class Faculty(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email, max_borrowed_books=10, borrow_days=30)

class Guest(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email, max_borrowed_books=1, borrow_days=7)