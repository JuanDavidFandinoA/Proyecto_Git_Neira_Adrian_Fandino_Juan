def menu_principal():
    print('''    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣦⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠙⠛⢿⣿⣿⠋⣄⠙⣿⣿⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠀⢸⣿⡟⠋⠁⠀⠉⠹⣿⠀⠀⠘⠉⠉⠛⢿⣿⣿⠀⢸⣿⣿⡟⠉⣠⣤⣄⠈⢿⣿⠏⢀⣴⣾⣿⣿⣦⡀⠹⣿⣦⣉⣠⣿⣿⣿⣿⣿⡷⠾⠿⣿⣿⣿⠉⠉⠙⠋⠉⠉⢻⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠛⠛⠁⣠⣾⡟⠀⠀⣾⣿⠀⠀⣿⠀⠀⢰⣿⣷⡀⠀⢻⣿⠀⢸⣿⡟⠀⣾⣿⣿⣿⠃⢸⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⣿⣿⣿⣿⡟⢉⣴⣶⠀⢸⣿⣿⣿⡇⢀⣾⣿⡆⠀⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡇⠀⢰⣿⡟⠀⠀⣿⠀⠀⢸⣿⣿⠃⠀⢸⣿⠀⢸⣿⡇⠐⣿⣿⣿⠋⠀⢸⣿⠀⠹⣿⣿⣿⣿⣿⡿⠿⣿⣿⠀⣿⣿⣿⡿⠀⣾⣿⡿⠀⣾⣿⣿⣿⡇⢸⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠿⠀⠀⠿⢿⣿⣿⣿⣧⠀⠈⠛⠁⢀⣼⣿⠀⠀⠈⠛⠋⠀⣠⣿⣿⠀⠘⢻⣷⡀⠙⠛⠁⣰⡄⢸⣿⣷⣀⠉⠛⠿⠛⠋⢀⣼⣿⣿⠀⢛⣿⣿⡇⠀⠻⠿⣁⣼⣿⣿⣿⠛⠃⠘⠛⡟⠃⠀⠛⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣷⣶⣾⣶⣶⣿⣿⣿⣿⣷⣶⣾⣿⣿⣷⣶⣿⣿⣷⣾⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣶⣶⣶⣶⣷⣶⣶⣶⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
    print(),
    print("Bienvenido a población! En este programa geografico podras visualizar, agregar y editar todo lo referentes a las ciudades del mundo, desde Bogotá hasta Nueva York")
    print("A continuación ingresa el número de la opción a la cual deseas acceder:")
    print('''
          1. Crear ciudades
          2. Editar ciudades
          3. Mostrar ciudades
          4. Buscar ciudades
          5. Salir''')
    
def pedir():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1

