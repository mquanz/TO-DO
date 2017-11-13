from tkinter import *
from tkinter import messagebox
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
        self.add_button.bind('<Button-3>', lambda event: self.message_box(event, 'This is the add button, please enter a task.'))
        self.add_button.grid(row = 1, column = 1)

        self.del_entry = Entry(master) 
        self.del_entry.grid(row = 2)

        self.del_button = Button(master, text = 'DELETE', bg = 'red')
        self.del_button.bind('<Button-1>', self.del_task)
        self.del_button.bind('<Button-3>', lambda event: self.message_box(event, 'This is the delete button, please enter a number.'))
        self.del_button.grid(row = 2, column = 1)

        self.text_box = Text(master, height = 10, width = 30)
        self.text_box.grid(row = 3)

        self.exit_button = Button(master, text = 'EXIT', command = master.quit)
        self.exit_button.grid(row = 4) 

    def message_box(self, event, text):
        messagebox.showinfo('Info', text)

    def add_task(self, event):
        user_input = self.add_entry.get()
        task_list1.insert_task(user_input)
        self.add_entry.delete(0, END)

#print list in text box

        self.text_box.delete(1.0, END)
        output_list = task_list1.print_list()
        self.text_box.insert(END, 'Your TO-DO-List:') 
        for task in output_list:
            self.text_box.insert(END, '\n' + task)    

    def del_task(self, event):
        user_input = int(self.del_entry.get())
        task_list1.delete_task(user_input)
        self.del_entry.delete(0, END)

#print list in text box

        self.text_box.delete(1.0, END)
        output_list = task_list1.print_list()
        self.text_box.insert(END, 'Your TO-DO-List:') 
        for task in output_list:
            self.text_box.insert(END, '\n' + task)    
        

root = Tk()
create_window = Window(root)
root.mainloop()
