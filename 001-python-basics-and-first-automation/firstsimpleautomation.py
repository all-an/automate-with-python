import os, time
import pyautogui
from datetime import date

today = date.today()
print("Today's date:", today)

#print('What is your age?')
#myAge = input()

#message = 'You will be ' + str(int(myAge) + 1) + ' in a year.'

message = "cd c:\\"

print(message)

os.system("start cmd")
time.sleep(0.5)

test = pyautogui.getWindowsWithTitle("cmd")[0]

test.maximize()

pyautogui.write(message, interval = 0.01)
pyautogui.press('enter')

pyautogui.write('explorer', interval = 0.01)
pyautogui.press('enter')

time.sleep(3)

test.close()

print(test)

#os.system("start chrome")

#pyautogui.write('python test.py', interval = 0.01)
#pyautogui.press('enter')