""" Todo List:
Create a Task class to represent a task in a todo list. 
Each task should have attributes like title, 
description, and status. 
Implement methods to mark a task as completed and display task information. """

class Tasks:
    def __init__(self,title,description,status):
        self.title= title
        self.description = description
        self.status = status

    def task_info(self):
            return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status_check()}\n"

    def status_check(self):
        if self.status == True:
            return "Completed"
        else:
            return "Not completed"
    
    def mark_as_completed(self):
        self.status = True
    

task1 = Tasks("Walkdog", "Take dog for a 30 min walk", False)
task2 = Tasks("Dishes", "TodoDishes", False)

print(task1.task_info())
print(task2.task_info())

print(f" O status da tarefa {task1.title}, é {task1.status_check()}")
print(f" O status da tarefa {task2.title}, é {task2.status_check()}")

#Marcar completa

task1.mark_as_completed()
task2.mark_as_completed()

print(f" O status da tarefa {task1.title}, é {task1.status_check()}")
print(f" O status da tarefa {task2.title}, é {task2.status_check()}")



""" print(task1.task_info())

# Mark task as completed
task1.mark_as_completed()
print(task1.status_check())
 """