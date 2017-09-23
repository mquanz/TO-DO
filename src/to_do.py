class Task:
    def __init__(self, description):
        self.description = description
        self.done = False 

task_list = []

def insert_element(description):
    task_list.append(Task(description))
    
def mark_done_element(number):
    task_list[number-1].done = True

def print_elements():
    number = 0
    for task in task_list:
        number = number + 1
        if task.done:
            status = '[x]'
        else:
            status = '[ ]'
        print(number,status,task.description)

def delete_element(number):
    task_list.pop(number - 1)


