import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame_top = tkinter.Frame(self.main_window)
        self.frame_bot = tkinter.Frame(self.main_window)


        self.label_t = tkinter.Label(self.frame_top,text='GPIO Test',fg = "red")
        self.label_b = tkinter.Label(self.frame_bot,text='Some stuff')

        self.label_t.pack()
        self.label_b.pack()

        self.frame_top.pack()
        self.frame_bot.pack()
        
        tkinter.mainloop()
        
my_gui = MyGUI()
