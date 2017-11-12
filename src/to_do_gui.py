from tkinter import *
from functions import *


task_list1 = TaskList()

class Window:

    def __init__(self, master):
        self.master = master
        master.title('TO-DO-List')

        self.label1 = Label(master, text = 'Welcome to TO-DO-List - made by Marterminator', font = ('Times', 14))
        self.label1.grid(row = 0, columnspan = 2)

        self.add_entry = Entry(master) 
        self.add_entry.grid(row = 1)

        self.add_button = Button(master, text = 'ADD')
        self.add_button.bind('<Button-1>', self.add_task)
        self.add_button.grid(row = 1, column = 1)

        self.exit_button = Button(master, text = 'EXIT', command = master.quit)
        self.exit_button.grid(row = 2) 

    def add_task(self, task):
        user_input = self.add_entry.get()
        task_list1.insert_task(user_input)

#optional print

        output_list = task_list1.print_list()
        for task in output_list:
            print(task)
        

root = Tk()
create_window = Window(root)
root.mainloop()
