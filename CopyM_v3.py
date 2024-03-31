import pyautogui
import pyperclip
import time


def format_pdf_text1(text):
    text = text.replace('\r', '\\r').replace('\n', '\\n').replace('-\\r\\n', '').replace('\\r\\n', ' ')
    return text

#改进2
def format_pdf_text(text):
    # 将PDF特有的连字符断行修复为完整的单词
    text = text.replace('-\n', '')
    
    # 然后我们将转换每一行，除了段落尾的空行
    formatted_lines = []
    lines = text.splitlines()
    for line in lines:
        if line.strip() == "":
            # 如果是空行，则判定为段落之间的换行，保留换行
            formatted_lines.append("\n")
        elif line.endswith('-'):
            # 如果一行以连字符结尾，则将其与下一行连接
            formatted_lines.append(line[:-1])
        else:
            # 如果不是以连字符结尾，添加一个空格进行连接
            formatted_lines.append(line + ' ')

    # 重新组合文本
    return ''.join(formatted_lines).strip()

# 改进3
def format_pdf_text3(text):
    # 修复被连字符断开的单词，并保留段落之间的换行
    text = text.replace('-\n', '')
    lines = text.splitlines()
    
    formatted_text = ""
    # 将断行的段落重新连接，但保留段落间的空行
    for i in range(len(lines)):
        if lines[i].strip() == "" and (i == 0 or lines[i-1].strip() == ""):
            # 跳过连续空白行之间的空行
            continue
        if lines[i].strip() == "":
            # 如果是单独的空行，则保留这个段落分隔
            formatted_text += '\n\n'
        else:
            if i + 1 < len(lines) and lines[i+1].strip() == "":
                # 当前行后面跟着空白行，应该是段落结尾
                formatted_text += lines[i] + '\n'
            else:
                # 普通行，合并到当前段落
                formatted_text += lines[i].strip() + ' '
    return formatted_text


import pyautogui
import pyperclip
import time

def monitor_mouse():
    last_x = pyautogui.position().x
    while True:
        try:
            time.sleep(0.1)  # Check every 100ms
            current_x = pyautogui.position().x
            if current_x < 20 and last_x > current_x:
                format_and_launch_saladict()
            last_x = current_x
        except:
            pass

def format_and_launch_saladict():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Wait for clipboard to update
    text = pyperclip.paste()
    if text:
        formatted_text = format_pdf_text(text)
        pyperclip.copy(formatted_text)
        pyautogui.hotkey('alt', 'l')
        pyautogui.keyUp('ctrl')  # 确保释放控制键
        print(formatted_text)
        print('\n')

if __name__ == '__main__':
    print('程序已启动，请将光标选中文本，然后快速移动到屏幕左侧区域以激活Saladict。')
    pyautogui.FAILSAFE = True
    monitor_mouse()