from pynput.keyboard import Controller
import time
import pyautogui
import keyboard as kb
import threading
from pystray import Icon
from PIL import Image, ImageDraw
import tkinter as tk

def crear_icono(color, nombre):
    # Crea una imagen cuadrada de 64x64 con un círculo del color dado
    imagen = Image.new('RGB', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(imagen)
    draw.ellipse((8, 8, 56, 56), fill=color)
    
    icon = Icon(nombre, imagen)
    icon.run()


keyboard = Controller()

POSICION_CARTA = (873, 971)
RGB_YELLOW = (212, 208, 0)


class Icono:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Sin bordes ni botones
        self.root.geometry("10x10+0+0")   # Tamaño mínimo y ubicado en esquina superior
        self.root.wm_attributes("-topmost", True)  # Siempre encima (si es necesario)
        self.root.wm_attributes("-alpha", 0.0)     # Inicialmente invisible (opacidad 0)

        self.canvas = tk.Canvas(self.root, width=10, height=10, highlightthickness=0)
        self.rect = self.canvas.create_rectangle(0, 0, 10, 10, fill='gray')
        self.canvas.pack()

        # Se ejecuta en segundo plano
        self.root.after(0, self.root.withdraw)  # Oculta la ventana inmediatamente
        self.root.mainloop()

    def cambiar_color(self, color):
        # Al cambiar color, hacemos visible un instante para que surta efecto
        self.root.deiconify()
        self.root.wm_attributes("-alpha", 1.0)
        self.canvas.itemconfig(self.rect, fill=color)
        self.root.update_idletasks()
        self.root.withdraw()  # La volvemos a ocultar

    def stop(self):
        self.root.destroy()

class Activador:
    def __init__(self):
        self.activado = False

    def swap(self):

        if self.activado:
            self.activado = False
            self.icono.cambiar_color('grey')
            print('Se desactivó la espera')
        else:
            self.activado = True
            self.icono.cambiar_color('yellow')
            print('esperando')



def press_W(keyboard=keyboard) -> None:
    keyboard.press('w')
keyboard.release('w')

def es_amarillo(color1, color2=RGB_YELLOW, threshold=20):
    return all(abs(c1 - c2) <= threshold for c1, c2 in zip(color1, color2))

activador = Activador()

def loop_w(activador):
    print('presione F1')
    while True:
        kb.wait('F1')
        activador.swap()

hilo_w = threading.Thread(target=loop_w, args=(activador, ), deamon=True)
hilo_w.start()

while True:
    time.sleep(0.05)
    if activador.activado:
        color_actual = pyautogui.screenshot().getpixel(POSICION_CARTA)
        if es_amarillo(color_actual):
            press_W(keyboard)
