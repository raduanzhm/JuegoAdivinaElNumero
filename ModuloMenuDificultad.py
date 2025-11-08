def Menudificultad():
    while True:
        print('--- Elige la dificultad ---')
        print(' 1. Facil (20 intentos)\n 2. Medio (12 intentos)\n 3. Dificil (5 intentos)')

        opcion = input('Selecciona la dificultad: ')

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                return 'Facil', 20
            elif opcion == 2:
                return 'Medio', 12
            elif opcion == 3:
                return 'Dificil', 5

        print('Opcion no valida. Intenta denuevo: ')
