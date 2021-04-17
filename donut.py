import time
import pyautogui

time.sleep(5)

a = open("words.txt", 'r')

for word in a:
    pyautogui.typewrite(word)
    pyautogui.press("enter")