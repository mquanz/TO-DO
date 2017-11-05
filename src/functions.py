import json
import time

FILENAME = 'data.txt'

class TaskList:

    def __init__(self):
        self.task_list = []
        self.creation_date = time.strftime("%d/%m/%Y")

    def insert_task(self, task):
        self.task_list.append(Task(task))

    def mark_done(self, number):
        self.task_list[number-1].done = True

    def print_list(self):
        number = 0
        for task in self.task_list:
            number = number + 1
            if task.done:
                status = '[x]'
            else:
                status = '[ ]'
            print(number, status, task.description)
        
class Task:

    def __init__(self, description, done = False):
        self.description = description
        self.done = done


#Test

#Create instance of TaskList
task_list1 = TaskList()

#Insert element and print
task_list1.insert_task('Test')

print(task_list1.task_list[0].description)

#Mark done element and print
task_list1.mark_done(1)

print(task_list1.task_list[0].done)

#Print
task_list1.print_list()


#def print_elements():
#    number = 0
#    for task in task_list:
#        number = number + 1
#        if task.done:
#            status = '[x]'
#        else:
#            status = '[ ]'
#        print(number,status,task.description)

def delete_element(number):
    task_list.pop(number - 1)

def serialize():
    dicts = [task.__dict__ for task in task_list]
    return json.dumps(dicts)

def deserialize(json_string):
    dicts = json.loads(json_string)
    tasks = []
    for dic in dicts:
        tasks.append(Task(dic['description'],dic['done']))
    task_list[:] = tasks

def export():
    obj = open(FILENAME, 'wb')
    obj.write(serialize().encode('utf-8'))
    obj.close

def importe():
    obj = open(FILENAME, 'r')
    deserialize(obj.read())
    obj.close

def clear_list():
    task_list[:] = []
