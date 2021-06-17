""" Reto 5 Vacunacion para Todos
    incorpora al modulo todos_vacuna.py
    Alejandro Tamayo
    Junio 5-2021 """

#---------------- Zona librerias------------
import todos_vacuna as tv

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 5")
    print("Vacunas:\n")
    print("1. Cargar datos ejemplo")
    print("2. Solicitar datos manual")
    print("3. Listar Datos")
    print("4. Buscar")
    print("5. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: 
        lista_pacientes=tv.datos_ejemplo()
    elif op==2: lista_pacientes=tv.solicitud_datos()
    elif op==3: tv.listar_datos(lista_pacientes)
    elif op==4: tv.busqueda(lista_pacientes)
    elif op==5: exit()
    else: print("Opción no valida, intente de nuevo")


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


"""
TODO
1. solicitar datos del paciente
    - documento
    - nombre
    - apellido
    - etapa del paciente
    - fecha nacimeinto
    - edad
    - fecha de cita
    - hora de cita
    - tipo de vacuna aplicada

2. Guardar tupla tipo paciente con los datos  ya
3. Guardar una lista de pacientes con la tupla   ya
4. contar el total de pacientes en la lista para el primer reporte
5. sacar los datos por cada tipo de vacuna
6. armar nuevas tuplas por tipo de vacuna
7. armar listas por vacuna.
8. sacar reporte por tipo de vacuna
"""