import pyqrcode
url = '--TYPE YOUR WEBSITE URL--' [like.../https//:www.google.com/]

k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)

