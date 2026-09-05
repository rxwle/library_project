from users.base_user import User

class Student(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email)
    
    def get_max_books(self):
        return 3
    
    def get_borrow_days(self):
        return 14
    
    def get_fine_per_day(self):
        return 0.7

class Faculty(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email)

    def get_max_books(self):
        return 10
    
    def get_borrow_days(self):
        return 30
    
    def get_fine_per_day(self):
        return 1.5

class Guest(User):
    def __init__(self, name: str, id: int, email: str):
        super().__init__(name, id, email)

    def get_max_books(self):
        return 1
    
    def get_borrow_days(self):
        return 7
    
    def get_fine_per_day(self):
        return 3