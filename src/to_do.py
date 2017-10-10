from functions import *
    
print('Welcome to TO-DO-List!')
print('Commands:')
print('"add: <element>": Add element to the TO-DO-List')
print('"print": Print the TO-DO-List')
print('"delete: <number>": Delete an element')
print('"mark: <number>": Mark done element')
print('"export": Export list in data.txt')
print('"import": Import list from data.txt')

while True:
    user_input = input('> ')
    x = user_input.find(':')
    if user_input[0:x] == 'add':
        x = x + 1
        while user_input[x] == ' ':
            x = x + 1
        insert_element(user_input[x:])
    elif user_input[0:x] == 'delete':
        x = x + 1
        while user_input[x] == ' ':
            x = x + 1
        delete_element(int(user_input[x:]))
    elif user_input[0:5] == 'print':
        print_elements()
    elif user_input[0:x] == 'mark':
        x = x + 1
        while user_input[x] == ' ':
            x = x + 1
        mark_done_element(int(user_input[x:]))
    elif user_input[0:6] == 'export':
        export()
    elif user_input[0:6] == 'import':
        importe()
    else:
        print('Please repeat the input.')
