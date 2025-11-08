import random

def JugarSolitario(intentos):
    print(f'[MODO SOLITARIO] Tienes {intentos} intentos.')
    numero = random.randint(1,1000)
    print('Adivina el numero.')

    for i in range(intentos + 1):
        n = int(input(f'Intento {i}: '))
        if n == numero:
            print(f'GANASTE El numero era {numero}.')
            return True, i, numero
        elif n < numero:
            print('El numero secreto es MAYOR.')
        else:
            print('El numero secreto es MENOR')
        restantes = intentos - i
        if restantes > 0: 
            print(f'Te quedan {restantes} intentos')

    print(f'PERDISTE : El numero secreto era {numero}.')
    return False, intentos, numero

def Jugar2Jugadores(intentos):
    print(f'[MODO 2 JUGADORES] Tienes {intentos} intentos.')
    print('JUGADOR 1, Escribe el numero secreto (1-1000): ')
    numero = int(input('Numero secreto: '))
    print ('\n' * 50)  

    for i in range(1, intentos + 1):
        n = int(input(f'[JUGADOR 2] Intento {i}: '))
        if n == numero:
            print(f'GANASTE El número era {numero}.')
            return True, i, numero
        elif n < numero:
            print('El número secreto es MAYOR.')
        else:
            print('El número secreto es MENOR.')
        restantes = intentos - i
        if restantes > 0:
            print(f'Te quedan {restantes} intentos')

    print(f'PERDISTE :( El número secreto era {numero}.')
    return False, intentos, numero