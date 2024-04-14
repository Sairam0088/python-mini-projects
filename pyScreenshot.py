# Taking Screenshots using pyscreenshot in Python
import pyscreenshot
import time

time.sleep(2)

image = pyscreenshot.grab()

image.show()

image.save('vscode.jpg')