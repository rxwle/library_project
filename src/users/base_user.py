class User():
    def __init__(self, name: str, id: int, email: str, max_borrowed_books: int, borrow_days: int, max_borrow_days: int, borrowed_books: list):
        
        errors = []
        if not(isinstance(name, str)):
            errors.append("Неверный тип name")
        if not(isinstance(email, str)):
            errors.append("Неверный тип name")
        if not(isinstance(borrow_days, int)):
            errors.append("Неверный тип name")
            
        if errors:
            report = "\n".join(errors)
            raise TypeError(f"{report}")
        
        self.name = name
        self.id = id
        self.email = email
        self.borrowedbooks = []
        self.max_borrowed_books = max_borrowed_books
        self.max_borrow_days = max_borrow_days
        self.borrow_days = borrow_days

    def _can_take_books(self):
        return len(self.borrowedbooks) < self.max_borrowed_books and self.borrow_days <= self.max_borrow_days

    