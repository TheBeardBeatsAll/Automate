import pyautogui, pyperclip, time

def getText():
    windows = pyautogui.getWindowsWithTitle('Notepad++')
    for window in windows:
        window.activate()
        pyautogui.click(window.left + 200, window.top + 200)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(5)
        text = pyperclip.paste()
        print(text)

if __name__ == "__main__":
    getText()