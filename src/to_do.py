import json

FILENAME = 'data.txt'

class Task:
    def __init__(self, description, done = False):
        self.description = description
        self.done = done

task_list = []

def insert_element(task_description):
       task_list.append(Task(task_description))
    
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

print('Welcome to TO-DO-List!')
print('You can add elements to the list by typing "add <element>", delete elements by typing delete <number>, print the TO-DO-List by typing "print"')

while True:
    user_input = input('> ')
    if user_input[0:3] == 'add':
        insert_element(user_input[4:])
    if user_input[0:6] == 'delete':
        delete_element(int(user_input[7:]))
    if user_input[0:5] == 'print':
        print_elements()
