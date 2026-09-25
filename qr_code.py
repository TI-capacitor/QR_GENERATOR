#Class that manages creation of qr codes
#exception handling should happen in main code
import qrcode
import os

class QR:
    #class constructor
    def __init__(self,url,img_name,file_path):
        self.url = url.strip()
        self.file_path = file_path.strip() #removes whitespace from the beginning and end of the string`
        self.img_name = img_name.strip()
        if not self.img_name.endswith(".png"):
            self.img_name += ".png"
        
        
        
    #generate qr code and save it to the specified file path
    def generate(self):
        qr = qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()
        self.full_path = os.path.join(self.file_path, self.img_name) #properly concatenates the file and image name
        img.save(self.full_path)

    # def success_message(self):
    #     print(f"QR code generated successfully, saved at {self.full_path}")