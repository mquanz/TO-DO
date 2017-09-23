task_list = []

def insert_elements(task):
    task_list.append(task)

def print_elements():
    number = 0
    for task in task_list:
        number = number + 1
        print(number,task)

def delete_element(number):
    task_list.pop(number - 1)

