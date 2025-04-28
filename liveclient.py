import requests
import time
import urllib3

# Endpoint | Información
# /allgamedata | Toda la información completa de la partida en un solo JSON.
# /playerlist | Lista de jugadores (sus nombres, campeones, stats).
# /playername | Tu propio nombre de invocador.
# /activeplayer | Tu propio estado (vida, maná, nivel, gold).
# /activeplayerabilities | Habilidades de tu campeón (cooldowns, niveles).
# /activeplayerrunepage | Runas activas que estás usando.
# /eventdata | Lista de eventos recientes (kills, torres destruidas).
# /gamestats | Datos generales: tiempo de juego, modo, mapa.

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def obtener_jugadores():
    url = 'https://127.0.0.1:2999/liveclientdata/playerlist'

    jugadores  = requests.get(url, verify=False).json()

    for jugador in jugadores:
        nombre = jugador.get("championName")
        print(nombre)
        print()

        for key in jugador.keys():
            print(key)

        print('\n\n\n\n')

start = time.perf_counter()

obtener_jugadores()

end = time.perf_counter()
print(f'Tiempo total de solicitud: {end - start}')