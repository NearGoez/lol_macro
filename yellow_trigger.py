from pynput.keyboard import Controller
import time
import pyautogui
import keyboard as kb
import threading
from PIL import Image, ImageDraw
from config import POSICION_CARTA, RGB_YELLOW
from models import Activador
from utils import press_w, f1_enabler

keyboard = Controller()

activador = Activador()


hilo_w = threading.Thread(target=loop_f1, args=(activador, ), daemon=True)
hilo_w.start()

while True:
    time.sleep(0.05)
    if activador.activado:
        color_actual = pyautogui.screenshot().getpixel(POSICION_CARTA)
        if es_amarillo(color_actual):
            press_W(keyboard)
