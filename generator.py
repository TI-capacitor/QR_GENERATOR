from py_compile import main
from tkinter import Tk, filedialog
from tkinter import *
import qrcode 
import os
import sys

#Class for handling GUI
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
        

#Class that manages creation of qr codes
#exception handling should happen in main code
class Qrcode:
    #class constructor
    def __init__(self,url,img_name,file_path):
        self.url = url.strip()
        self.file_path = file_path.strip() #removes whitespace from the beginning and end of the string`
        self.img_name = img_name.strip()
        if not self.img_name.endswith(".png"):
                    self.img_name += ".png"
        
        
        
    #generate qr code and save it to the specified file path
    def get_qr(self):
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()
        self.full_path = os.path.join(self.file_path, self.img_name) #properly concatenates the file and image name
        img.save(self.full_path)

    def success_message(self):
        print(f"QR code generated successfully, saved at {self.full_path}")

gui = GUI()
gui.show_window()  #opens window for user to select directory
directory_path = gui.get_directory()

if not directory_path: #exiting pressing the x button on the GUI leaves the directory path empty, causing the program to close
    print("Goodbye!!!")
    sys.exit()



while pngEmpty:
    pngName = input("Enter the name you want for your code:")  #strip() removes whitespace from the beginning and end of the string
    
    if pngName:
        print(f"Name entered for image {pngName}")
        pngEmpty = False
        
    else:
        print("ERROR: name of picture cannot be blank")

#Validate user input for url

while urlEmpty: 
    url = input("Enter the URL you want to generate a QR code for: ") #strip() removes whitespace from the beginning and end of the string

    if url:
        print(f"URL entered for QR code {url}")
        urlEmpty = False

    else:
        print("ERROR: URL cannot be blank")

qr = Qrcode(url, pngName, directory_path)  #create instance of QR class
qr.get_qr() #creates qr code with path provided by window GUI
qr.success_message()








