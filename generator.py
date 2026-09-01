from tkinter import Tk, filedialog
from tkinter import *
import qrcode 
import os

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
        self.file_path = filedialog.askdirectory() #prompts user for file path
        self.close_window() 

    def get_directory(self):
        return self.file_path #returns file path

    def close_window(self):
        self.window.destroy() #closes window upon choosing directory
        

#Class that manages creation of qr codes
#exception handling should happen in main code
class Qrcode:
    #class constructor
    def __init__(self,url,img_name,file_path):
        self.url = url
        self.file_path = file_path
        self.img_name = img_name + ".png"

    #generate qr code and save it to the specified file path
    def get_qr(self):
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()
        self.full_path = os.path.join(self.file_path, self.img_name) #properly concatenates the file and image name
        img.save(self.full_path)

    def success_message(self):
        print("QR code generated successfully, saved at {}".format(self.full_path))


pngNotEmpty = True
gui = GUI()
gui.set_directory()
directory_path = gui.get_directory()

while(pngNotEmpty):
    pngName = input("Enter the name you want for your code:").strip()    
    
    if pngName:
        print("Name entered for image {}".format(pngName))
        pngNotEmpty = False
        
    else:
        print("ERROR: name of picture cannot be blank")

#Validate user input for url
url = input("Enter the URL you want to generate a QR code for: ")
qr = Qrcode(url, pngName, gui.get_directory())  #create instance of QR class
qr.get_qr() #creates qr code with path provided by window GUI
qr.success_message()











