import qrcode


#Path were qr codes generated will be stored for now
file_path = "C:\\Users\\test\\OneDrive - Inter American University of Puerto Rico - Bayamon Campus\\Desktop\\Interamericana\\2026-2027\\QR_GENERATOR\\qr_codes\\dantutoringqr.png"
url = input("Enter your url: ").strip()

print(url)

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated")