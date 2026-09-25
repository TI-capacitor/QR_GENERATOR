#Class for handling GUI
from tkinter import Tk, filedialog
from tkinter import *


class GUI:
    def __init__(self):
        self.window = Tk()
        self.button = Button(text="Open Directory",command=self.set_directory)  #creates clickable button, command calls the get_directory method
        self.button.pack()
        self.file_path = ""

    def show_window(self):
        self.window.mainloop() 
        
    def set_directory(self):
        print("Opening file dialog")
        self.file_path = filedialog.askdirectory() #prompts user for file dialog box, line that may fail

        if not self.file_path: #if the user presses cancel or enters a empty url, let them know
            print("User pressed cancel")
        else:
            self.window.destroy()

        print("Filedalog is closing...")

    def get_directory(self):
        return self.file_path #returns file path
        


