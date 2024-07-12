from menus import *
from datos import *

ciudades_DB = "ciudades.json"
datos_ciudades = traer_datos(ciudades_DB)

while True:
    menu_principal()
    opc = pedir()
    if opc == 1:
        print("menu usuarios")
    elif opc == 2:
        print("editar ciudades")
    elif opc == 3:  
        print("Salió!!")
        break
