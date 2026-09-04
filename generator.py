from py_compile import main
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
        try:
            self.file_path = filedialog.askdirectory() #prompts user for file dialog box, line that may fail

            if not self.file_path: #if the user presses cancel or enters a empty url, let them know
                print("No URL entered!!!")
  
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

        finally: #closes file dialog box
            self.window.destroy()

        
    
    def get_directory(self):
        return self.file_path #returns file path
        

#Class that manages creation of qr codes
#exception handling should happen in main code
class Qrcode:
    #class constructor
    def __init__(self,url,img_name,file_path):
        self.url = url
        self.file_path = file_path
        self.img_name = img_name
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
        print("QR code generated successfully, saved at {}".format(self.full_path))


url = ""
pngName = ""
pngEmpty = True
urlEmpty = True


gui = GUI()
gui.show_window()  #opens window for user to select directory
directory_path = gui.get_directory()

while(pngEmpty):
    pngName = input("Enter the name you want for your code:").strip()   #strip() removes whitespace from the beginning and end of the string

    
    if pngName:
        print("Name entered for image {}".format(pngName))
        pngEmpty = False
        
    else:
        print("ERROR: name of picture cannot be blank")

#Validate user input for url


while(urlEmpty): 
    url = input("Enter the URL you want to generate a QR code for: ").strip()  #strip() removes whitespace from the beginning and end of the string

    if url:
        print("URL entered for QR code {}".format(url))
        urlEmpty = False

    else:
        print("ERROR: URL cannot be blank")

qr = Qrcode(url, pngName, directory_path)  #create instance of QR class
qr.get_qr() #creates qr code with path provided by window GUI
qr.success_message()


# if __name__ == "__main__":
#     main()








