import qrcode

data = "rudal madarchot"

# Create an instance of the QRCode class
qr = qrcode.QRCode(version=3, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an instance of the QRCodeImage class
img1 = qr.make_image(fill_color="purple", back_color="white")

# Save the generated QR code image
img1.save('1.png')

