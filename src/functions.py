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
        output_list = []
        for task in self.task_list:
            number = number + 1
            if task.done:
                status = '[x]'
            else:
                status = '[ ]'
            output_list.append(str(number) + ' ' + status + ' ' + task.description)
        return output_list

    def delete_task(self, number):
        self.task_list.pop(number-1)

    def serialize(self):
        dicts = [task.__dict__ for task in self.task_list]
        dicts.append({"creation" : self.creation_date})
        return json.dumps(dicts)

    def deserialize(self, json_string):
        dicts = json.loads(json_string)
        tasks = []        
        for dic in dicts:
            if 'description' in dic.keys():
                tasks.append(Task(dic['description'],dic['done']))
            else:
                self.creation_date = dic['creation']
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

    def info(self):
        print('This TaskList was created at ' + self.creation_date + ' and contains ' + str(len(self.task_list)) + ' tasks.')
        
class Task:

    def __init__(self, description, done = False):
        self.description = description
        self.done = done
