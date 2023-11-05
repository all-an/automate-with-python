import pyautogui

my_pillow = pyautogui.screenshot()

print(type(my_pillow))

# 'C:\\Users\\Public\\code\\automate-with-python\\015-gui-automation'

path = 'C:\\Users\\Public\\code\\automate-with-python\\015-gui-automation\\example_screenshot.png'

pyautogui.screenshot(path)


# locate on screen

file_path = 'C:\\Users\\Public\\code\\automate-with-python\\015-gui-automation\\seven_button.png'

locale1 = pyautogui.locateOnScreen(file_path)

print(type(locale1))

print(locale1)

print(pyautogui.locateCenterOnScreen(file_path))

pyautogui.moveTo((1430,593), duration=1)

pyautogui.click()