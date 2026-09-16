class Student:
    def __init__(self, name, age, specialty):
        self.__name = name
        self.__age = age
        self.__specialty = specialty

    def show_info(self):
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Специальность: {self.__specialty}")

    def change_specialty(self, new_specialty):
        self.__specialty = new_specialty


student = Student("Аян", 18, "Программная инженерия")

student.show_info()

student.change_specialty("Кибербезопасность")

print("\nПосле изменения:")
student.show_info()