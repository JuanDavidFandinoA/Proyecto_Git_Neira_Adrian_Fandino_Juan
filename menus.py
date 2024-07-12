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
    opcion1 = int(input("Opción:"))
    if opcion1 != int("1"):
        print("Error. Se ha introducido una opción no valida. Intente nuevamente.")


menu_principal()
pedir()
