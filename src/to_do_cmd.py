from functions import *
    
print('Welcome to TO-DO-List!\n')
help = 'Commands:\n"add <element>": Add element to the TO-DO-List\n"print": Print the TO-DO-List\n"delete <number>": Delete an element\n"mark <number>": Mark done element\n"export": Export list in data.txt\n"import": Import list from data.txt\n"clear": Clear list\n"info": Information about this list\n"help": List of commands\n"quit": Quit program'
print(help)
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
        for task in show_list(my_list):
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
    elif user_input == 'help':
        print(help)
    elif user_input == 'quit':
        break
    else:
        print('Invalid input. Type "help" to see possible commands.')
