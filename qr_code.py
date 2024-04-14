# qr code generator using pyqrcode module

import pyqrcode
import os

youtube = "https://www.youtube.com/@Develop_with_Python-hf3ro"

qr_code = pyqrcode.create(youtube)

qr_code.svg("develop_with_python.svg", scale=8)

os.startfile("develop_with_python.svg")