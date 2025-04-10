import pyautogui
import time

time.sleep(2)

x, y = pyautogui.position()
rgb = pyautogui.screenshot().getpixel((x, y))

print(f"Posición actual del mouse: ({x}, {y})")
print(f'Color RGB en esa posicion: {rgb}')
