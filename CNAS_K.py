import time
import pyperclip
from pynput.keyboard import Key, Controller, KeyCode, Listener
# from pynput import mouse

def keyboard_press(Key1,Key2):
    with keyboard.pressed(Key1):
        keyboard.press(Key2)
        keyboard.release(Key2)
        
def on_press(key):  
    if key == Key.ctrl_l:
        keyboard_press(Key.ctrl,'c')
        return False

def on_release(key):  
    if key == Key.ctrl_l:
        keyboard_press(Key.ctrl,'c')
        return False

copyedTemp='temp'
keyboard = Controller()
print('准备就绪，请复制')
while True:
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
        
    copyedText = pyperclip.paste()
    time.sleep(0.001)
    if copyedTemp != copyedText:
        copyedText = copyedText.replace("\r", "\\r").replace("\n", "\\n").replace("-\\r\\n", "").replace("\\r\\n", " ")
        time.sleep(0.1)
        pyperclip.copy(copyedText)
        copyedTemp=copyedText
        keyboard_press(Key.alt,'l')
        
    else:
        pass
