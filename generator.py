from tkinter import Tk, filedialog
from tkinter import *
import qrcode 
import os

filepath = ""

#Class that manages creation of qr codes and saving path
class Qrcode:
    #class constructor
    def __init__(self,url,img_name):
        self.url = url
        self.img_name = img_name

    #generate qr code and save it to the specified file path
    def generate_qr(self, file_path):
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()

        self.full_path = os.path.join(file_path, self.img_name) #properly concatenates the file and image name
        img.save(self.full_path)

    def success_message(self):
        print("QR code generated successfully, saved at {}".format(self.full_path))

########
def openFile():
    global filepath
    filepath = filedialog.askdirectory()
    window.destroy() #file dialog window upon selection of folders

#Placeholder class for handling GUI
class GUI:
    def __init__(self,file_path):
        self.file_path = file_path

    def openFile():
        self.file_path = filedialog.askdirectory()
        window.destroy() #file dialog window upon selection of folders

    def closeFile():
        pass
        

# This will go in the GUI class
window = Tk()
button = Button(text="Open Directory",command=openFile)
button.pack()
window.mainloop()
#

pngName = input("Enter the name you want for your code:")
pngName += ".png"


#need to add exception handling for invalid url
url = input("Enter the URL you want to generate a QR code for: ")


qr = Qrcode(url, pngName)  #create instance of QR class
qr.generate_qr(filepath) #creates qr code with path provided by window GUI
qr.success_message()
print(filepath)

