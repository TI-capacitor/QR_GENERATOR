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



#Path were qr codes generated will be stored for now

pngName = input("Enter the name you want for your code (must end in .png)")
url = input("Enter your url: ").strip()

qr_code = QR(url, pngName)
qr_code.generate_qr(filepath)
qr_code.success_message()

