# Лабораторная работа №13
# Задание 16. Планировщик задач
# Титов Даниэль, ИС 25-22

from collections import deque

normal_tasks = deque()
urgent_tasks = deque()

def add_task(name, urgent=False):
    if urgent:
        urgent_tasks.append(name)
        print("Добавлена срочная задача:", name)
    else:
        normal_tasks.append(name)
        print("Добавлена обычная задача:", name)

def process_task():
    if urgent_tasks:
        task = urgent_tasks.popleft()
        print("Выполнена срочная задача:", task)

    elif normal_tasks:
        task = normal_tasks.popleft()
        print("Выполнена обычная задача:", task)

    else:
        print("Нет задач для выполнения.")

def show_tasks():
    print("Срочные задачи:", list(urgent_tasks))
    print("Обычные задачи:", list(normal_tasks))


add_task("Подготовить отчёт")
add_task("Исправить ошибку", True)
add_task("Проверить программу")
add_task("Срочная проверка", True)

show_tasks()

print("\nОбработка задач:")
process_task()
process_task()
process_task()
process_task()
process_task()