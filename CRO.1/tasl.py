
from dataclasses import dataclass, asdict
import json


@dataclass
class Student:
    name: str
    subject: str
    rating1: float
    rating2: float
    exam: float

    def calculate_rating(self):
        average = (self.rating1 + self.rating2) / 2
        return average * 0.60 + self.exam * 0.40


def input_grade(message):
    while True:
        try:
            grade = float(input(message).replace(",", "."))
            if 0 <= grade <= 100:
                return grade
            print("Ошибка: оценка должна быть от 0 до 100.")
        except ValueError:
            print("Ошибка: введите число.")


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    return "F"


def add_student(students):
    name = input("Имя студента: ").strip()
    subject = input("Название предмета: ").strip()

    if not name or not subject:
        print("Ошибка: имя и предмет не могут быть пустыми.")
        return

    rating1 = input_grade("Первый рейтинг (0-100): ")
    rating2 = input_grade("Второй рейтинг (0-100): ")
    exam = input_grade("Экзамен (0-100): ")

    student = Student(name, subject, rating1, rating2, exam)
    students.append(student)

    result = student.calculate_rating()
    print(f"\nИтоговый рейтинг: {result:.2f}")
    print(f"Буквенная оценка: {get_letter_grade(result)}")


def show_students(students):
    if not students:
        print("Список студентов пуст.")
        return

    print("\n--- Результаты студентов ---")

    for number, student in enumerate(students, start=1):
        result = student.calculate_rating()
        print(
            f"{number}. {student.name} | "
            f"{student.subject} | "
            f"Рейтинг: {result:.2f} | "
            f"Оценка: {get_letter_grade(result)}"
        )


def search_student(students):
    query = input("Введите имя для поиска: ").strip().casefold()

    if not query:
        print("Введите имя для поиска.")
        return

    found = [
        student for student in students
        if query in student.name.casefold()
    ]

    if found:
        show_students(found)
    else:
        print("Студент не найден.")


def save_students(students):
    filename = input("Имя файла [ratings.json]: ").strip()
    if not filename:
        filename = "ratings.json"

    try:
        data = []

        for student in students:
            record = asdict(student)
            record["final_rating"] = round(
                student.calculate_rating(), 2
            )
            data.append(record)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Результаты успешно сохранены.")

    except OSError as error:
        print(f"Ошибка сохранения: {error}")


def main():
    students = []

    while True:
        print("\n=== Калькулятор академического рейтинга ===")
        print("1. Добавить студента")
        print("2. Показать результаты")
        print("3. Найти студента")
        print("4. Сохранить результаты")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            save_students(students)
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Введите число от 1 до 5.")


if __name__ == "__main__":
    main()
