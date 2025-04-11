import threading
from config import RGB_CUADRO_NIVEL_ENEMIGO
from models import Activador
from utils import (enemigos_en_pantalla, f1_enabler,
                   auto_kiter, pyautogui, py_keyboard,
                   extraer_attack_speed)
import time



a = Activador()
t1 = threading.Thread(target=f1_enabler, args=(a,), daemon=True)
t1.start()

auto_kiter(a)


