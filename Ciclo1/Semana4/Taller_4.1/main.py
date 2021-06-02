""" Modulo Principal
    Funciones para practicas con ciclos
    Alejandro Tamayo
    Mayo 29-2021 """

import funciones_ciclos as fc

def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido a la Miscelanea de ejercicios Taller 4.1")
    print("Seleccione el algoritmo a verificar:\n")
    print("1. Caida Libre")
    print("2. Generaciones")
    print("3. Constructor de Triangulos")
    print("4. Generador de Tableros")
    print("5. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: fc.simulador_caida_libre()
    elif op==2: fc.generador_generaciones()
    elif op==3: fc.constructor_triangulos()
    elif op==4: fc.constructor_tableros()
    elif op==5: exit()
    else: print("Opción no valida, intente de nuevo")