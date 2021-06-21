""" Reto 7 Informes de Vacunacion
    incorpora al modulo visualizacion_datos.py
    Alejandro Tamayo
    Junio 21-2021 """

#---------------- Zona librerias------------

import visualizacion_datos as vd
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
#IV_07_RS_01
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 7")
    print("Reportes con Información Real sobre Covid-19 en Colombia\n")
    print("La información se toma desde la página de datos Our World in Data, através de un archivo CSV actualizado diariamente\n")
    print("Seleccione una opción\n")
    print("1. Cargar datos desde CSV")
    print("2. Menú Gráficos")
    print("3. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: 
        datos = vd.leer_archivo()
    elif op==2: vd.graficos_menu(datos)
    elif op==3: exit()
    else: print("Opción no válida, intente de nuevo")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


