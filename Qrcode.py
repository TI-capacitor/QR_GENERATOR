
class QR:
    import qrcode 

    #class constructor
    def __init__(self,url,img_name):
        self.url = url
        self.img_name = img_name

    #generate qr code and save it to the specified file path
    def generate_qr(self, file_path):
        import os
        qr = self.qrcode.QRCode()
        qr.add_data(self.url)
        img = qr.make_image()

        full_path = os.path.join(file_path, self.img_name) #properly concatenates the file and image name
        img.save(full_path)

    def success_message(self):
        print("QR code generated successfully!")
