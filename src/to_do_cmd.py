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
print('"info": Information about this list')
print('"quit": Quit program')

my_list = TaskList()
print('\nWith starting this program you just created a new list at ' + my_list.creation_date + '!')

while True:
    user_input = input('> ')
    position = user_input.find(':')
    if user_input[0:position] == 'add':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        my_list.insert_task(user_input[position:])
    elif user_input[0:position] == 'delete':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        my_list.delete_task(int(user_input[position:]))
    elif user_input == 'print':
        output_list = show_list(my_list)
        for task in output_list:
            print(task)        
    elif user_input[0:position] == 'mark':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        my_list.mark_done(int(user_input[position:]))
    elif user_input == 'export':
        my_list.export()
    elif user_input == 'import':
        my_list.importe()
    elif user_input == 'clear':
        my_list.clear_list()
    elif user_input == 'info':
        print(my_list.info())
    elif user_input == 'quit':
        break
    else:
        print('Please repeat the input.')
