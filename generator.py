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


pngName = input("Enter the name you want for your code (must end in .png)")
try:
   if pngName.endswith(".png"):
       pass
   else:
       raise ValueError("File name must end with .png")

except ValueError as e:
    print(f"Error: {e}")

url = input("Enter the URL you want to generate a QR code for: ")

qr_code = QR(url, pngName)
qr_code.generate_qr(filepath)
qr_code.success_message()
print(filepath)

