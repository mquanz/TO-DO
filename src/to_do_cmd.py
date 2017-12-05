from functions import *
    
print('Welcome to TO-DO-List!\n')
print('Commands:')
print('"add <element>": Add element to the TO-DO-List')
print('"print": Print the TO-DO-List')
print('"delete <number>": Delete an element')
print('"mark <number>": Mark done element')
print('"export": Export list in data.txt')
print('"import": Import list from data.txt')
print('"clear": Clear list')
print('"info": Information about this list')
print('"quit": Quit program')

my_list = TaskList()
print('\nWith starting this program you just created a new list at ' + my_list.creation_date + '!')

while True:
    user_input = input('> ')
    user_list = user_input.split(' ')
    if user_list[0] == 'add':
        my_list.insert_task(user_list[1])
    elif user_list[0] == 'delete':
        my_list.delete_task(int(user_list[1]))
    elif user_input == 'print':
        output_list = show_list(my_list)
        for task in output_list:
            print(task)        
    elif user_list[0] == 'mark':
        my_list.mark_done(int(user_list[1]))
    elif user_input == 'export':
        export(my_list)
    elif user_input == 'import':
        importe(my_list)
    elif user_input == 'clear':
        my_list.clear_list()
    elif user_input == 'info':
        print(info(my_list))
    elif user_input == 'quit':
        break
    else:
        print('Please repeat the input.')
