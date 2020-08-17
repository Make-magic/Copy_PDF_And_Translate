import time
import pyperclip
from pynput.keyboard import Key, Controller, KeyCode
# from pynput import mouse

def keyboard_press(Key1,Key2):
    with keyboard.pressed(Key1):
        keyboard.press(Key2)
        keyboard.release(Key2)
        
# def on_move(x, y):
#     if x <= 0:
#         keyboard_press(Key.ctrl,'c')
#         return False

copyedTemp=' '
keyboard = Controller()
print('准备就绪，请复制')
while True:
#     with mouse.Listener(on_move=on_move) as listener:
#         listener.join()
        
    copyedText = pyperclip.paste()
    time.sleep(0.001)
    if copyedTemp != copyedText:
        copyedTemp=copyedText
        copyedText = copyedText.replace("\r", "\\r").replace("\n", "\\n").replace("-\\r\\n", "").replace("\\r\\n", " ")
        time.sleep(0.2)
        pyperclip.copy(copyedText)
        keyboard_press(Key.alt,'l')

    else:
        pass