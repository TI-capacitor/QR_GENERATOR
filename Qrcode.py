import qrcode 

class QR:
    
    def __init__(self,url,img_name):
        self.url = url
        self.img_name = img_name


    def generate_qr(self, file_path):
        qr = self.qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()
        img.save(file_path + self.img_name)

    def success_message(self):
        print("QR code generated successfully!")
