import pyqrcode # pip install pyqrcode
from PIL import Image # IMPORT pip install pypng

name = input('Enter a name for the QR: ')
link = input('Enter the link to generate the QR: ')
qrcode = pyqrcode.create(link)
qrcode.png(name + ".png", scale=5)
Image.open("QRCode.png")