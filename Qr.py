import pyqrcode
url = 'https://physiotherapist123.000webhostapp.com/'

k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)

