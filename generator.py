import sys
from gui import GUI
from qr_code import QR
import qrcode

gui = GUI()
gui.show_window()  #opens window for user to select directory
directory_path = gui.get_directory()

if not directory_path: #exiting pressing the x button on the GUI leaves the directory path empty, causing the program to close
    print("Goodbye!!!")
    sys.exit()


while True:
    pngName = input("Enter the name you want for your code:")  #strip() removes whitespace from the beginning and end of the string
    if pngName:
        print(f"Name entered for image {pngName}")
        break

    print("ERROR: name of picture cannot be blank")

#Validate user input for url

while True: 
    url = input("Enter the URL you want to generate a QR code for: ") #strip() removes whitespace from the beginning and end of the string
    if url:
        print(f"URL entered for QR code {url}")
        break
    
    print("ERROR: URL cannot be blank")

qr = QR(url, pngName, directory_path)  #create instance of QR class
qr.get_qr() #creates qr code with path provided by window GUI
qr.success_message()








