import pymem
import pymem.process

pm = pymem.Pymem("League of Legends.exe")

module = pymem.process.module_from_name(pm.process_handle, "League of Legends.exe")
base_address = module.lpBaseOfDll

oLocalPlayer = 0x2F43900 

local_player = pm.read_int(base_address + oLocalPlayer)

oHealth = 0xE7C  

health = pm.read_float(local_player + oHealth)

print(f"Salud del jugador: {health}")
