from Qrcode import QR
#Path were qr codes generated will be stored for now
file_path = "C:\\Users\\Dani\\Desktop\\"
pngName = input("Enter the name you want for your code (must end in .png)")
url = input("Enter your url: ").strip()

qr_code = QR(url, pngName)
qr_code.generate_qr(file_path)
qr_code.success_message()

