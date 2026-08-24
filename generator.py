from Qrcode import QR
from tkinter import Tk, filedialog
from tkinter import *

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


qr_code = QR(url, pngName)  #create instance of QR class
qr_code.generate_qr(filepath) #creates qr code with path provided by window GUI
qr_code.success_message()
print(filepath)