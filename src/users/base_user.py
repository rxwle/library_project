class User():
    def __init__(self, name: str, id: int, email: str):
        
        errors = []
        if not(isinstance(name, str)):
            errors.append("Неверный тип name")
        if not(isinstance(email, str)):
            errors.append("Неверный тип name")
            
        if errors:
            report = "\n".join(errors)
            raise TypeError(f"{report}")
        
        self.name = name
        self.id = id
        self.email = email
        self.borrowedbooks = []

    def get_max_books(self):
        raise NotImplementedError
    
    def get_borrow_days(self):
        raise NotImplementedError
    
    def get_fine_per_day(self):
        raise NotImplementedError

    def can_take_books(self):
        return len(self.borrowedbooks) < self.get_max_books()
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}({self.id})\nEmail:{self.email}"

    