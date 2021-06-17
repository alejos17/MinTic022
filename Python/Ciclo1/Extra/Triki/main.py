"""
Para este juego vamos a usar un tablero de 3x3, en el cual el jugador,
llámese "X" o "O" va a ingresar el número correspondiente al sitio en el cual
desea poner su ficha. El tablero es el siguiente:
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
"""


def formatear_tablero(juego) -> str:
    formato_fila = '| {} | {} | {} |'  # formato de cada fila del tablero
    bar = '-------------'  # línea divisoria
    tablero = "\n"  # inicializa el tablero en fin de linea (return)
    tablero = tablero.join([bar, formato_fila.format(*juego[:3]), bar,
                            formato_fila.format(*juego[3:6]), bar,
                            formato_fila.format(*juego[6:]), bar])

    # La funcion join concatena todos los elementos de la lista y los separa con el caracter \n
    return tablero


def actualizar_movimiento(juego, jugada, jugador) -> str:
    # Validación del tipo y el rango de la jugada
    if not (jugada.isdigit() and int(jugada) in range(1, 10)):  # Condiciones que debe cumplir
        print(f'Jugada no válida "{jugada}", Solo ingrese valores entre  1-9')
        return juego  # El juego no cambia

    # Validación de jugada permitida
    numero_jugada = int(jugada)
    if juego[numero_jugada - 1] in 'XO':  # Esta ocupada con otra jugada
        print(f'La casilla "{jugada}" ya esta ocupada')
        return juego  # El juego no cambia

    # actualiza el juego con la nueva jugada
    juego = juego[:numero_jugada - 1] + jugador + juego[numero_jugada:]
    return juego


def encontrar_ganador(juego) -> str:
    # Opciones de ganar el juego representadas con tuplas
    ganadores = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                 (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for jugador in ('X', 'O'):  # Verificar por cada jugador
        for i, j, k in ganadores:  # buscar por cada opción ganadora en la lista de ganadores
            linea = (juego[i], juego[j], juego[k])  # obtiene una tupla de los simbolos en las posiciones
            if linea == (jugador, jugador, jugador):  # compara si la tupla tiene el simbolo del jugador
                return jugador
    return None  # No hay ganador


def jugar_triqui() -> None:
    juego = "123456789"  # Inicia el tablero sin jugadas
    jugador = 'X'  # Inicia el jugador X
    while True:  # Ciclo infinito
        print(formatear_tablero(juego))  # Dibuja el tablero
        jugada = input(f'Jugador {jugador}, ¿Cual es la jugada? [q para terminar]: ')

        if jugada == 'q':  # Se retira
            print("Has perdido por W")
            break

        juego = actualizar_movimiento(juego, jugada, jugador)  # actualiza el tablero
        ganador = encontrar_ganador(juego)  # Busca al ganador

        if ganador != None:  # hay un ganador
            print(f"{ganador} has ganado!")
            print(formatear_tablero(juego))
            break

        if jugador == 'X':  # Cambia el símbolo del jugador para la próxima jugada
            jugador = 'O'
        else:
            jugador = 'X'

# ====================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# ===================================================================


jugar_triqui()
"""
tupla = (0,1,2)
print(type(tupla))
i,j,k = tupla

print(i)
print(j)
print(k)


lista = ["juan","carlos","miguel","pedro"]
print(lista)
lista = "\n".join(lista)
print(lista)



formato_fila = "| {} | {} | {} |"
linea = "123456789"
bar = '-------------'
print(bar)
print(formato_fila.format(*linea[:3]))
print(bar)
print(formato_fila.format(*linea[3:6]))
print(bar)
print(formato_fila.format(*linea[6:]))
print(bar)
"""