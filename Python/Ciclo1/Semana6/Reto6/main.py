""" Reto 6 Informes de Vacunacion
    incorpora al modulo informe_vacuna.py
    Alejandro Tamayo
    Junio 13-2021 """

#---------------- Zona librerias------------
import informe_vacuna as iv
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#----------Definición de Funciones (Dividir)------------
#IV_06_RS_01
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 6")
    print("Vacunas:\n")
    print("1. Cargar datos ejemplo")
    print("2. Graficos Generales")
    print("3. Graficos Específicos")
    print("4. Listar Datos")
    print("5. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: lista_pacientes=iv.leer_archivo()
    elif op==2: iv.graficos_gral(lista_pacientes)     
    elif op==3: iv.graficos_esp(lista_pacientes)
    elif op==4: iv.listar_datos(lista_pacientes)
    elif op==5: exit()
    else: print("Opción no válida, intente de nuevo")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================