import pyautogui
import pyperclip
import time

class AC_saladict():
    def __init__(self):
        self.size = pyautogui.size()
        self.pos = pyautogui.position()

    def copy(self):
        global tem_text
        global text
        if self.pos[0] < 10:
            pyautogui.hotkey('ctrl','c')
            text = pyperclip.paste().replace("\r", "\\r").replace("\n", "\\n").replace("-\\r\\n", "").replace("\\r\\n", " ")
            if tem_text != text:
                tem_text = text
                self.convey_saladict()
            
    def convey_saladict(self):
        pyperclip.copy(tem_text)
        pyautogui.hotkey('alt','l')
        print(tem_text)
            
if __name__ == '__main__':
    tem_text = ''
    text = ''
    print('准备就绪，请复制')
    pyautogui.FAILSAFE = True
    while True:
        try:
            time.sleep(0.1)
            AC_saladict().copy()
        except:
            pass
