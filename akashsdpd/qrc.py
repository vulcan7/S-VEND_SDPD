#import pyqrcode
#qr = pyqrcode.create("HORN O.K. PLEASE.")
#qr.jpg("horn.jpg", scale=6)
import qrtools
qr = qrtools.QR()
qr.decode("horn.jpg")
print qr.data
