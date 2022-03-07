import numpy as np
from pyzbar.pyzbar import decode
import cv2

#Reading QR Code from an Image
img = cv2.imread("C:/Users/MACHIRA/Downloads/images.png")
code = decode(img)
print(code)

for barcode in decode(img):
    print(barcode.data )#in bytes
    text = barcode.data.decode('utf-8')
    print(text)
    print(barcode.rect)
