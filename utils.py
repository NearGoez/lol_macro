import keyboard
import time
import pyautogui
from PIL import Image, ImageDraw, ImageGrab
from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Controller
from models import Activador
from config import *

py_keyboard = Controller()
py_mouse = mouse_controller()

def left_click_retorno(x, y, mouse=py_mouse):
    posicion_inicial = mouse.position
    
    mouse.position = (x +50, y+75)
    pyautogui.mouseDown(button='right')

    pyautogui.mouseUp(button='right')
    
    mouse.position = posicion_inicial

def f1_enabler(activador: Activador) -> None:
    print('presione F1')
    while True:
        keyboard.wait('F1')
        activador.swap()

def es_amarillo(color1, color2=RGB_YELLOW, threshold=20):
    return all(abs(c1 - c2) <= threshold for c1, c2 in zip(color1, color2))

def press_w(py_keyboard=py_keyboard) -> None:
    py_keyboard.press('w')
    py_keyboard.release('w')

def es_rojo_oscuro(color1, color2=RGB_CUADRO_NIVEL_ENEMIGO, threshold=1):
    if all(abs(c1 - c2) <= threshold for c1, c2 in zip(color1, color2)):
        return True

def enemigos_en_pantalla(RGB_CUADRO_NIVEL=(52, 3, 0)) -> list:
    start = time.perf_counter()

    campeones_en_pantalla = []

    screenshot = ImageGrab.grab()
    pixeles = screenshot.load()

    ancho, alto = screenshot.size

    for j in range(0, alto, 14):
        for i in range(0, ancho, 14):
            if es_rojo_oscuro(pixeles[i, j]):
                campeones_en_pantalla.append((i, j))
                print(i, j)
    end = time.perf_counter()

    print(end - start)
    return campeones_en_pantalla

def auto_atacar(x: int, y: int) -> None:
    campeones = enemigos_en_pantalla()
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    distancia_mas_cercana = float('inf')

    posicion_mas_cercana = (0, 0)

    for coordenada in campeones:
        x_c, y_c = coordenada
        distancia_actual = (x_c - x)**2 + (y_c - y)**2

        if distancia_actual <= distancia_mas_cercana:
            posicion_mas_cercana = coordenada
            distancia_mas_cercana = distancia_actual

    if posicion_mas_cercana != (0, 0):
        print(posicion_mas_cercana)
        left_click_retorno(*posicion_mas_cercana)

def auto_kiter(activador: Activador) -> None:
    print(TIEMPO_ENTRE_BASICOS)
    while True:
        time.sleep(0.01)
        if activador.activado:
            py_keyboard.press('a')
            py_keyboard.release('a')
            time.sleep(TIEMPO_ENTRE_BASICOS/3)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            time.sleep(max(TIEMPO_ENTRE_BASICOS * (2/4) - 0.01, 0))

def loop_x() -> None:
    print('X para Golpear al enemigo mas cercano')
    while True:
        keyboard.wait('x')
        x, y = pyautogui.position()
        auto_atacar(x, y)
