""" Programa Saltando al 5
    Realiza codificación y decodificación 
    de mensajes
    incorpora al modulo csi.py
    Alejandro Tamayo
    Junio 2-2021 """

#---------------- Zona librerias------------
import csi as c
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Taller 5.2")
    print("=======================================================\n")
    msg=input("Escriba el mensaje: ")
    print("\n")
    print("Que desea hacer?: ")
    print("1. Codificar / Decodificar")
    print("2. Escribir otro mensaje a codificar")
    print("3. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    print(" ")
    return op,msg

#Bandera para entar al bucle del menú
flag=1
while flag==1:
    op,msg=menu()
    if op==1: 
        c.codificar_mensaje(msg)
    elif op==2: 
        print(" ")
        msg=input("Escriba el nuevo mensaje: ")
        c.codificar_mensaje(msg)
    elif op==3: 
        exit()
    else: print("Opción no valida, intente de nuevo")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================