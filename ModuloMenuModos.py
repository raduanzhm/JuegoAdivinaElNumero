def MenuPrincipal():
    while True:
        print('--- Modo de Juego ---')
        print(' 1. Solitario \n 2. 2 Jugadores \n 3. Estadisticas \n 4. Salir')
       
        modo = input('Opcion: ')
       
        if modo.isdigit():
            modo = int(modo)
            if 1 <= modo  <= 4:
                return modo
       
        print('Opcion no valida. Intenta de nuevo: ')

