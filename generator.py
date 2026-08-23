import qrcode


#Path were qr codes generated will be stored for now
file_path = "C:\\Users\\test\\OneDrive - Inter American University of Puerto Rico - Bayamon Campus\\Desktop\\Interamericana\\2026-2027\\QR_GENERATOR\\qr_codes\\"
pngName = input("Enter the name you want for your code (must end in .png)")
file_path += pngName
url = input("Enter your url: ").strip()


#declaration of qr object of type 'qrcode' 
qr = qrcode.QRCode()

#use the object qr to add the url entered by user with the add_data() method
qr.add_data(url)

#.make_image() generates the image embedded with the url entered
img = qr.make_image()

#.save() method saves the 
img.save(file_path)

#successful run of code
print("QR code was generated succesfullly")