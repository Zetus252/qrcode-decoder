import cv2
from pyzbar.pyzbar import decode

image = cv2.imread('put your qrcode path here')

decode_data = decode(image)

if decode_data:
    for code in decode_data:
        decoded_text = code.data.decode('utf-8')
        print(f'Decoded Text: {decoded_text}')

else:
    print("No QR code found or could not be decoded")