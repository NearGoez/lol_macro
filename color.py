

import pyautogui
import time

time.sleep(1)

x, y = pyautogui.position()
rgb = pyautogui.screenshot().getpixel((846, 483))

print(f"Posición actual del mouse: ({x}, {y})")
print(f'Color RGB en esa posicion: {rgb}')
