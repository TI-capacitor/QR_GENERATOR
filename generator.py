from tkinter import Tk, filedialog
from tkinter import *
import qrcode 
import os



######
class qrcode:
   

    #class constructor
    def __init__(self,url,img_name):
        self.url = url
        self.img_name = img_name

    #generate qr code and save it to the specified file path
    def generate_qr(self, file_path):
        
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()

        full_path = os.path.join(file_path, self.img_name) #properly concatenates the file and image name
        img.save(full_path)

    def success_message(self):
        print("QR code generated successfully!")
########

def openFile():
    global filepath
    filepath = filedialog.askdirectory()

window = Tk()
button = Button(text="Open Directory",command=openFile)
button.pack()
window.mainloop()


pngName = input("Enter the name you want for your code:")
pngName += ".png"


#need to add exception handling for invalid url
url = input("Enter the URL you want to generate a QR code for: ")


qr = QR(url, pngName)  #create instance of QR class
qr.generate_qr(filepath) #creates qr code with path provided by window GUI
qr.success_message()
print(filepath)