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
        self.add_entry.insert(0, 'Enter a task here...')
        self.add_entry.config(fg = 'grey')
        self.add_entry.bind('<Button-1>', lambda event: self.entry_click(event, 'Enter a task here...', self.add_entry))
        self.add_entry.grid(row = 1)

        self.add_button = Button(master, text = 'ADD', bg = 'green')
        self.add_button.bind('<Button-1>', self.add_task)
        self.add_button.bind('<Button-3>', lambda event: self.message_box(event, 'This is the add button, please enter a task.'))
        self.add_button.grid(row = 1, column = 1)

        self.del_entry = Entry(master) 
        self.del_entry.insert(0, 'Enter a number here...')
        self.del_entry.config(fg = 'grey')
        self.del_entry.bind('<Button-1>', lambda event: self.entry_click(event, 'Enter a number here...', self.del_entry))
        self.del_entry.grid(row = 2)

        self.del_button = Button(master, text = 'DELETE', bg = 'orange')
        self.del_button.bind('<Button-1>', self.del_task)
        self.del_button.bind('<Button-3>', lambda event: self.message_box(event, 'This is the delete button, please enter a number.'))
        self.del_button.grid(row = 2, column = 1)

        self.mark_button = Button(master, text = 'MARK', bg = 'light blue')
        self.mark_button.bind('<Button-1>', self.mark_task)
        self.mark_button.bind('<Button-3>', lambda event: self.message_box(event, 'This is the mark button, please enter a number.'))
        self.mark_button.grid(row = 3, column = 1)

        self.mark_entry = Entry(master) 
        self.mark_entry.insert(0, 'Enter a number here...')
        self.mark_entry.config(fg = 'grey')
        self.mark_entry.bind('<Button-1>', lambda event: self.entry_click(event, 'Enter a number here...', self.mark_entry))
        self.mark_entry.grid(row = 3)

        self.clear_button = Button(master, text = 'CLEAR', bg = 'red')
        self.clear_button.bind('<Button-1>', self.warning_box)
        self.clear_button.grid(row = 5, column = 1)

        self.info_button = Button(master, text = 'INFO', bg = 'yellow')
        self.info_button.bind('<Button-1>', lambda event: self.message_box(event, task_list1.info()))
        self.info_button.grid(row = 4, column = 1)

        self.export_button = Button(master, text = 'EXPORT', bg = 'green')
        self.export_button.bind('<Button-1>', self.export)
        self.export_button.grid(row = 5, column = 0)

        self.import_button = Button(master, text = 'IMPORT', bg = 'green')
        self.import_button.bind('<Button-1>', self.importe)
        self.import_button.grid(row = 6, column = 0)

        self.text_box = Text(master, height = 10, width = 30)
        self.text_box.grid(row = 4)

        self.exit_button = Button(master, text = 'EXIT', bg = 'red', command = master.quit)
        self.exit_button.grid(row = 6, column = 1) 

    def entry_click(self, event, default_text, entry):
        if entry.get() == default_text:
            entry.delete(0, END)
            entry.config(fg = 'black')

    def message_box(self, event, text):
        messagebox.showinfo('Info', text)

    def warning_box(self, event):
        result = messagebox.askquestion('Clear', 'Are You Sure?', icon = 'warning')
        if result == 'yes':
            self.clear_tasks()

    def print_tasks(self):
        self.text_box.delete(1.0, END)
        output_list = task_list1.print_list()
        self.text_box.insert(END, 'Your TO-DO-List:') 
        for task in output_list:
            self.text_box.insert(END, '\n' + task)    

    def add_task(self, event):
        user_input = self.add_entry.get()
        task_list1.insert_task(user_input)
        self.add_entry.delete(0, END)
        self.print_tasks()  

    def del_task(self, event):
        user_input = int(self.del_entry.get())
        task_list1.delete_task(user_input)
        self.del_entry.delete(0, END)
        self.print_tasks()
        
    def mark_task(self, event):
        user_input = int(self.mark_entry.get())
        task_list1.mark_done(user_input)
        self.mark_entry.delete(0, END)
        self.print_tasks()

    def clear_tasks(self):
        task_list1.clear_list()    
        self.print_tasks()

    def export(self, event):
        task_list1.export()
        self.message_box(event, 'Your Task List is written to data.txt')  

    def importe(self, event):
        task_list1.importe() 
        self.print_tasks()     

root = Tk()
create_window = Window(root)
root.mainloop()
