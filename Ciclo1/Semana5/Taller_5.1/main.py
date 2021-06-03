""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#---------------- Zona librerias------------
import smarth_home as sh

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def datos_ejemplo():
    comando="Sensor Sala,humedad,ON@Alarma,movimiento,ON@Lampara,Luces,ON@Sensor Cocina,Temperatura,OFF@Alarma Puerta,apertura,ON@Sensor Habitacion,Temperatura,OFF@Interruptor,luces,ON"
    return comando

def recibir_datos():
    comando=input("Comando a recibir: ")
    return comando

def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Taller 5.1")
    print("IoT:\n")
    print("1. Cargar datos ejemplo")
    print("2. Cargar datos manual")
    print("3. Correr programa")
    print("4. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: comando=datos_ejemplo()
    elif op==2: comando=recibir_datos()
    elif op==3: 
        lista_IoT=sh.separar_cadenas(comando)
        print("\n")
        print("La Lista de Tuplas es: ",lista_IoT)
        sh.calcular_estadisticas(lista_IoT)
    elif op==4: exit()
    else: print("Opción no valida, intente de nuevo")
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================