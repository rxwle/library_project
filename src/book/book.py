class Book():
    def __init__(self, title: str, author: str):

        errors = []
        if not(isinstance(title, str)):
            errors.append("Неверный тип title")
        if not(isinstance(author, str)):
            errors.append("Неверный тип author")
            
        if errors:
            report = "\n".join(errors)
            raise TypeError(f"{report}")
        
        self.title = title
        self.author = author
        self.available_status = True

    def __str__(self):
        status = "в наличии" if self.available_status else "занята"
        return f"Книга: {self.author} '{self.title}' {status}"