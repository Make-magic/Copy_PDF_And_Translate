import pyperclip
import time
print('准备就绪，请复制')
while True:
    time.sleep(2)
    copyedText = pyperclip.paste()
    if True:
        changedText = copyedText.replace("\r", "\\r").replace("\n", "\\n").replace("-\\r\\n", "").replace("\\r\\n", " ")
        pyperclip.copy(changedText)