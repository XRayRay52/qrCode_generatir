import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="black")
    img.save(file_name)

text = "https://www.nike.com/t/air-jordan-1-retro-high-og-mens-shoes-JHpxkn/DZ5485-400"
file_name = "qrCodeimage.bmp"
generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")