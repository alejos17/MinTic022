""" Reto 7 Informes de Vacunacion
    incorpora al modulo visualizacion_datos.py
    Tu nombre aquí
    Junio XX-XX """

#---------------- Zona librerias------------

import visualizacion_datos as vd
import pandas as pd
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
#IV_06_RS_01
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 7")
    print("Reportes con Información Real sobre Covid-19 en Colombia\n")
    print("La información se toma desde la página de datos abiertos del Gobierno Nacional para la utilización de datos para estadisticas\n")
    print("Seleccione una opción\n")
    print("1. Cargar datos ejemplo desde CSV")
    print("2. Cargar todos los datos desde datos.gov.co")
    print("3. Graficos")
    print("4. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: 
        datos = vd.leer_archivo()
        print(datos)
        print(type(datos))
    elif op==2: exit()
    elif op==3: vd.grafico_tendencia(datos)
    elif op==4: exit()
    else: print("Opción no válida, intente de nuevo")



#vd.graficador(datos)

#print(datos.columns)
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


