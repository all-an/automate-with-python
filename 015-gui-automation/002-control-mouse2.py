import pyautogui, time, os

pyautogui.moveRel(0, 300, duration=0.5)

pyautogui.moveRel(300, 0, duration=0.5)

pyautogui.click(642, 1052)

time.sleep(2)

pyautogui.write('Paint')

time.sleep(1)

pyautogui.click(656, 428)

time.sleep(4)

pyautogui.moveTo(959, 591)

distance = 200

while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1) # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1) # down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1) # left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1) # up


