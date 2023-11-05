import pyautogui, time

print(pyautogui.size())

width, height = pyautogui.size()

print(width)

print(height)

mouse_position = (1,1)

while mouse_position[0] != 0:
    mouse_position_now = pyautogui.position()
    if mouse_position != mouse_position_now:
        mouse_position = mouse_position_now
        print('X = ' + str(mouse_position[0]))
        print('Y = ' + str(mouse_position[1]))
        print(mouse_position)
        
pyautogui.displayMousePosition()

pyautogui.moveTo(1435, 297)

time.sleep(1)

pyautogui.moveTo(369, 370, duration=0.5)

