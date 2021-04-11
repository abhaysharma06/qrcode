import pyqrcode
from pyqrcode import QRCode
s="https://codeforgrow.github.io/teamhotwire.github.io/"
url=pyqrcode.create(s)
url.svg("QrCode.svg",scale=10)
