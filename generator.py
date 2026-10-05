import sys
from gui import GUI
from qr_code import QR

gui = GUI()
gui.show_window()  #opens window for user to select directory
directory_path = gui.get_directory()

if not directory_path: #exiting pressing the x button on the GUI leaves the directory path empty, causing the program to close
    print("Goodbye!!!")
    sys.exit()


while True:
    png_name = input("Enter the name you want for your code:")  #strip() removes whitespace from the beginning and end of the string
    if png_name:
        print(f"Name entered for image {png_name}")
        break

    print("ERROR: name of picture cannot be blank")

#Validate user input for url

while True: 
    url = input("Enter the URL you want to generate a QR code for: ") #strip() removes whitespace from the beginning and end of the string
    if url:
        print(f"URL entered for QR code {url}")
        break

    print("ERROR: URL cannot be blank")

qr = QR(url, png_name, directory_path)  #create instance of QR class
qr.generate() #creates qr code with path provided by window GUI
qr.success_message()








