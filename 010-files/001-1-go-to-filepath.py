import os, time
import pyautogui

path = "cd c:\\"

""" os.system("start cmd")
time.sleep(0.5) """

pyautogui.write(path, interval = 0.5)

#time.sleep(0.5)
pyautogui.press('enter')

path2 = "cd Users\\Public\\code\\automate-with-python\\010-files"

pyautogui.write(path2)

time.sleep(0.5)
pyautogui.press('enter')

print(path2)

""" time.sleep(2)
pyautogui.write(path2, interval = 1)

#time.sleep(0.5)
pyautogui.press('enter') """