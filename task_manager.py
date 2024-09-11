# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return f"Задача '{description}' отмечена как выполненная."
        return f"Задача '{description}' не найдена."

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        return pending_tasks

    def display_pending_tasks(self):
        print("Текущие (не выполненные) задачи:")
        for task in self.get_pending_tasks():
            print(task)


# Создание экземпляра класса TaskManager и выполнение операций
task_manager = TaskManager()
task_manager.add_task("Оформить проект", "2024-09-01")
task_manager.add_task("Сдать проект", "2024-11-05")

# Отметим задачу как выполненную
print(task_manager.mark_task_completed("Сдать проект"))

# Отобразим текущие (не выполненные) задачи
task_manager.display_pending_tasks()
