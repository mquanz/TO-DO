from tkinter import *


class Window:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.label1 = Label(frame, text = 'Welcome to TO-DO-List', bg = 'black', fg = 'white')
        self.label1.grid(row = 0)

        self.exit_button = Button(frame, text = 'Exit', command = frame.quit)
        self.exit_button.grid(row = 1) 


root = Tk()
create_window = Window(root)
root.mainloop()
