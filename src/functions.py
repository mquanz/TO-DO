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

    def print_list(self):
        number = 0
        for task in self.task_list:
            number = number + 1
            if task.done:
                status = '[x]'
            else:
                status = '[ ]'
            print(number, status, task.description)

    def delete_task(self, number):
        self.task_list.pop(number-1)

    def serialize(self):
        dicts = [task.__dict__ for task in self.task_list]
        return json.dumps(dicts)

    def deserialize(self, json_string):
        dicts = json.loads(json_string)
        tasks = []
        for dic in dicts:
            tasks.append(Task(dic['description'],dic['done']))
        self.task_list = tasks

    def export(self):
        obj = open(FILENAME, 'wb')
        obj.write(self.serialize().encode('utf-8'))
        obj.close

    def importe(self):
        obj = open(FILENAME, 'r')
        self.deserialize(obj.read())
        obj.close

    def clear_list(self):
        self.task_list = []
        
class Task:

    def __init__(self, description, done = False):
        self.description = description
        self.done = done
