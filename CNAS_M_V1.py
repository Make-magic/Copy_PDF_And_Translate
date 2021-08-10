import time
import pyperclip
from pynput.keyboard import Key, Controller, KeyCode
from pynput import mouse
#
def keyboard_press(Key1,Key2):
    with keyboard.pressed(Key1):
        keyboard.press(Key2)
        keyboard.release(Key2)
        
def on_move(x, y):
    if x <= 0:
        keyboard_press(Key.ctrl,'c')
        print('yes')
        return False

copyedTemp=' '
keyboard = Controller()
print('准备就绪，请复制')
while True:
    time.sleep(0.1)
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
        
    copyedText = pyperclip.paste()
    time.sleep(0.1)
    if copyedTemp != copyedText:
        copyedText = copyedText.replace("\r", "\\r").replace("\n", "\\n").replace("-\\r\\n", "").replace("\\r\\n", " ")
        pyperclip.copy(copyedText)
        copyedTemp = copyedText
        keyboard_press(Key.alt,'l')

    else:
        pass
