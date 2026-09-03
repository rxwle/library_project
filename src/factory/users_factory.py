from users.users import Student, Faculty, Guest

class UsersFactory():
    @staticmethod
    def user_create(name: str, id: int, email: str, role: str):
        if role == "Student":
            user = Student(name, id, email)
        elif role == "Faculty":
            user = Faculty(name, id, email)
        elif role == "Guest":
            user = Guest(name, id, email)
        else:
            raise ValueError("Нет такой роли")
        return user
