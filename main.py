import qrcode

def generate_qrcode(text):
    """
    Generates a QR code for a given text and saves it as an image.

    This function creates a QR code image for the specified text. It sets up 
    the QR code with certain parameters like version, error correction level, 
    box size, and border. The QR code is then populated with the data from 
    the input text. Finally, the QR code image is saved as 'QRimg.png'.

    Parameters:
    text (str): The text to be converted into a QR code.

    Returns:
    None: The function saves the QR code as an image file and does not return anything.
    """

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fir=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save("QRimg.png")

url = input("Enter your url: ")
generate_qrcode(url)