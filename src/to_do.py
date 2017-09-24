import json

FILENAME = 'data.txt'

class Task:
    def __init__(self, description, done = False):
        self.description = description
        self.done = done

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

def serialize():
    dicts = [task.__dict__ for task in task_list]
    json_string = json.dumps(dicts)
    obj = open(FILENAME, 'wb')
    obj.write(json_string.encode('utf-8'))
    obj.close

def deserialize(json_string):
    dicts = json.loads(json_string)
    tasks = []
    for dic in dicts:
        tasks.append(Task(dic['description'],dic['done']))
    task_list[:] = tasks
