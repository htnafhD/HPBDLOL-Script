import pyautogui as p
import time
import win32gui
import keyboard

"""Please place the code.txt file and this execute file in the same place!"""


def find_Running(WindowName):
    try:
        var = win32gui.FindWindow(None, WindowName)
        win32gui.SetForegroundWindow(var)
        return 1
    except Exception as e:
        return 0


def handle_Mouse():
    p.moveTo(1176, 565)
    p.click()
    time.sleep(3)
    with open(r'path\code.txt', 'r', encoding='utf-8') as f:
        f_content = f.readlines()
        for data in f_content:
            if keyboard.is_pressed('F12'):
                break
            else:
                p.click(1049, 778, clicks=2)
                time.sleep(0.1)
                p.typewrite(data)
                time.sleep(0.1)
                p.click(881, 684, clicks=2)


def main():
    find_Running('League of Legends')
    handle_Mouse()


if __name__ == "__main__":
    main()
