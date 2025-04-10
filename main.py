import pyautogui
import win32api
import win32con
import time
import random
import subprocess
from press import press_key, release_key


CENTRO_PANTALLA_XY = (891, 496)
TIEMPO_DORMIR = 1/1.72


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def centered_random_movement(centro = CENTRO_PANTALLA_XY):
    posicion_xy = [*centro]
    cantidad_movimiento = random.randint(200, 400)

    direccion_x = random.choice(['-', '+'])
    direccion_y = random.choice(['-', '+'])
    
    if direccion_x == '-':
        posicion_xy[0] -= cantidad_movimiento
    else:
        posicion_xy[0] += cantidad_movimiento

    if direccion_y == '-':
        posicion_xy[1] -= cantidad_movimiento
    else:
        posicion_xy[1] += cantidad_movimiento
           
    win32api.SetCursorPos(posicion_xy)  


time.sleep(2)
VK_A = 0x41  # Código de la tecla 'A'
while True:
    
    centered_random_movement()
    subprocess.run(['press_a.exe'])
    time.sleep(TIEMPO_DORMIR)

    
