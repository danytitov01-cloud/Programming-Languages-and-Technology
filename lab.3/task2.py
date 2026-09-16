class Course:
    def __init__(self, name, teacher, students=None):
        self.__name = name
        self.__teacher = teacher
        self.__students = students if students else []

    def add_student(self, student):
        self.__students.append(student)

    def show_students(self):
        print(f"Курс: {self.__name}")
        print(f"Преподаватель: {self.__teacher}")
        print("Студенты:")
        for student in self.__students:
            print("-", student)


course = Course("Python", "Иванов И.И.")

course.add_student("Аян")
course.add_student("Данияр")
course.add_student("Алина")

course.show_students()
