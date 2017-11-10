import tkinter

root = tkinter.Tk()

class main():
    def __init__(self):
        rahmen = tkinter.Frame()
        text = tkinter.Label(rahmen, text='Welcome to TO-DO-List!')
        text.pack()
        rahmen.pack()
     
main()
root.mainloop()
