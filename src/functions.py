import json
import time

FILENAME = 'data.txt'

class TaskList:

    def __init__(self):
        self.task_list = []
        self.creation_date = time.strftime("%d/%m/%Y %H:%M")

    def insert_task(self, task):
        self.task_list.append(Task(task))

    def mark_done(self, number):
        self.task_list[number-1].done = True

    def delete_task(self, number):
        self.task_list.pop(number-1)

    def clear_list(self):
        self.task_list = []
                
class Task:

    def __init__(self, description, done = False):
        self.description = description
        self.done = done

def show_list(instance):
    number = 0
    output_list = []
    for task in instance.task_list:
        number = number + 1
        if task.done:
            status = '[x]'
        else:
            status = '[ ]'
        output_list.append(str(number) + ' ' + status + ' ' + task.description)
    return output_list

def serialize(instance):
    dicts = [task.__dict__ for task in instance.task_list]
    dicts.append({"creation" : instance.creation_date})
    return json.dumps(dicts)

def deserialize(instance, json_string):
    dicts = json.loads(json_string)
    tasks = []        
    for dic in dicts:
        if 'description' in dic.keys():
            tasks.append(Task(dic['description'],dic['done']))
        else:
            instance.creation_date = dic['creation']
    instance.task_list = tasks
    return instance

def export(instance):
    obj = open(FILENAME, 'wb')
    obj.write(serialize(instance).encode('utf-8'))
    obj.close

def importe(instance):
    obj = open(FILENAME, 'r')
    deserialize(instance, obj.read())
    obj.close

def info(instance):
    return 'This TaskList was created at ' + instance.creation_date + ' and contains ' + str(len(instance.task_list)) + ' tasks.'
