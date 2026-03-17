""" Generatin QRcode """

#Authors: Chatgpt and weiguang yang

import qrcode
from PIL import Image

# URL

# Step 1: Create the QR code
url = "https://pypi.org/project/micromechanics-indentationGUI/"

qr = qrcode.QRCode(
    version=1,  # Adjust version based on QR code complexity
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to compensate for the logo
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)

qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Step 2: Open the logo image
logo = Image.open('logo.png')  # Replace with the path to your logo

# Step 3: Resize the logo to fit within the QR code
qr_width, qr_height = qr_img.size
logo_size = int(qr_width / 4)  # Logo should take up roughly 1/4th of the QR code
logo = logo.resize((logo_size, logo_size))

# Step 4: Calculate the position to paste the logo (centered)
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Step 5: Overlay the logo on the QR code
qr_img.paste(logo, logo_position, mask=logo)

# Step 6: Save the final QR code with the logo
qr_img.save('indentationGUI_QRcode.png')

# Optionally, display the image
#qr_img.show()
