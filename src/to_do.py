from functions import *
    
print('Welcome to TO-DO-List!\n')
print('Commands:')
print('"add: <element>": Add element to the TO-DO-List')
print('"print": Print the TO-DO-List')
print('"delete: <number>": Delete an element')
print('"mark: <number>": Mark done element')
print('"export": Export list in data.txt')
print('"import": Import list from data.txt')
print('"clear": Clear list')
print('"quit": Quit program')

task_list = TaskList()
print('\nWith starting this program you just created a new list at ' + task_list.creation_date + '!')

while True:
    user_input = input('> ')
    position = user_input.find(':')
    if user_input[0:position] == 'add':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        task_list.insert_task(user_input[position:])
    elif user_input[0:position] == 'delete':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        task_list.delete_task(int(user_input[position:]))
    elif user_input == 'print':
        task_list.print_list()
    elif user_input[0:position] == 'mark':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        task_list.mark_done(int(user_input[position:]))
    elif user_input == 'export':
        task_list.export()
    elif user_input == 'import':
        task_list.importe()
    elif user_input == 'clear':
        task_list.clear_list()
    elif user_input == 'quit':
        break
    else:
        print('Please repeat the input.')
