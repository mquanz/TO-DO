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

        self.add_button = Button(master, text = 'ADD', bg = 'green')
        self.add_button.bind('<Button-1>', self.add_task)
        self.add_button.grid(row = 1, column = 1)

        self.del_entry = Entry(master) 
        self.del_entry.grid(row = 2)

        self.del_button = Button(master, text = 'DELETE', bg = 'red')
        self.del_button.bind('<Button-1>', self.del_task)
        self.del_button.grid(row = 2, column = 1)

        self.print_button = Button(master, text = 'PRINT')
        self.print_button.bind('<Button-1>', self.print_tasks)
        self.print_button.grid(row = 3)

        self.text_box = Text(master, height = 10, width = 30)
        self.text_box.grid(row = 4)

        self.exit_button = Button(master, text = 'EXIT', command = master.quit)
        self.exit_button.grid(row = 5) 

    def add_task(self, arg):
        user_input = self.add_entry.get()
        task_list1.insert_task(user_input)
        self.add_entry.delete(0, END)     

    def del_task(self, arg):
        user_input = int(self.del_entry.get())
        task_list1.delete_task(user_input)
        self.del_entry.delete(0, END)

    def print_tasks(self, arg):
        self.text_box.delete(1.0, END)
        output_list = task_list1.print_list()
        self.text_box.insert(END, 'Your TO-DO-List:')
        for task in output_list:
            self.text_box.insert(END, '\n' + task)
        

root = Tk()
create_window = Window(root)
root.mainloop()
