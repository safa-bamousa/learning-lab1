class Task:
    def __init__(self, title, descreption, due_date, status):
        self.title = title
        self.descreption = descreption
        self.due_date = due_date
        self.status = status
    
    def display_task(self):
        print(f"Title: {self.title}")
        print(f"Descreption: {self.descreption}")
        print(f"Due date: {self.due_date}")
        print(f"Status: {self.status}")

    def mark_as_complete(self):
        self.status = "complete"
        
task1 = Task("Review Syntax","Review how to create a class and an pbject","2026-02-18","incompleted")
task1.display_task()
task1.mark_as_complete()
task1.display_task()