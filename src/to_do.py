from functions import *
    
print('Welcome to TO-DO-List!')
print('Commands:')
print('"add: <element>": Add element to the TO-DO-List')
print('"print": Print the TO-DO-List')
print('"delete: <number>": Delete an element')
print('"mark: <number>": Mark done element')
print('"export": Export list in data.txt')
print('"import": Import list from data.txt')
print('"clear": Clear list')
print('"quit": Quit program')

while True:
    user_input = input('> ')
    position = user_input.find(':')
    if user_input[0:position] == 'add':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        insert_element(user_input[position:])
    elif user_input[0:position] == 'delete':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        delete_element(int(user_input[position:]))
    elif user_input == 'print':
        print_elements()
    elif user_input[0:position] == 'mark':
        position = position + 1
        while user_input[position] == ' ':
            position = position + 1
        mark_done_element(int(user_input[position:]))
    elif user_input == 'export':
        export()
    elif user_input == 'import':
        importe()
    elif user_input == 'clear':
        clear_list()
    elif user_input == 'quit':
        break
    else:
        print('Please repeat the input.')
