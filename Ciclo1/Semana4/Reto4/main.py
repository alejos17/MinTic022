""" Reto 4 Citas para Vacunacion  #
    incorpora al modulo cita_vacunas.py
    Alejandro Tamayo
    Mayo 29-2021 """
#---------------- Zona librerias------------

import cita_vacunas as cv
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
pacientes=[]   #Inicialización de listas
citasdisponibles=[]
#----------Definición de Funciones (Dividir)------------
def bienvenida():
    """ 
    Parameters
    ----------
    Se realiza impresión en pantalla de mensaje de bienvenida
    """
    print(" ")
    print(" ")
    print("Bienvenido al Reto 4, Semana 4 de MicTIC2022")
    print("esta pequeña aplicación intenta resolver el siguiente problema\n")
    print("Asignación de citas para Vacunación\n")
    print("En base a los pacientes y etapas ingresados, se asignan las citas requeridas desde el 25 de Mayo en un horario de 10:00 a 12:00\n\n")
    print("Con los datos que vamos a solicitar a continuación evaluaremos la solución propuesta\n\n")

def menu():
    """ 
    Parameters
    ----------
    Se realiza impresión de menú en pantalla
    ----------
    Returns
    ----------
    op:int
        Retorna el valor del menú seleccionado por el usuario
    """
    print("======================================================")
    print("Bienvenido, por favor selecione una opción: \n")
    print("1. Mostrar la lista de pacientes con sus etapas ingresadas")
    print("2. Priorizar la lista de pacientes por etapas")
    print("3. Realizar asignación de citas y mostrar el listado total")
    print("4. Buscar por nombre de paciente")
    print("5. Salir\n")
    op=int(input("Por favor indique la opción: "))
    return op
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================
bienvenida()    #Inicio del programa

#Pregunta para cargar datos de ejemplo o cargarlos manual, para pruebas
print("Antes de continuar para probar el programa de forma rapida")
z=int(input("Quiere colocar datos de ejemplo?: 1.Si  2.No (Asignar pacientes manualmente):  "))
if z==1:
    print("\n")
    pacientes=cv.datos_ejemplo()
    print("Se han cargado los datos de 40 pacientes de ejemplo con sus etapas")
else:
    print("\n")
    print("En esta opción vamos a cargar cada paciente manualmente: \n")
    pacientes=cv.actualizando()

flag=1

while flag==1:
    op=menu()
    if op==1: 
        print("\n")
        print("La Lista de pacientes agregados es:\n")
        print(pacientes)
        print("\n")
    elif op==2: 
        pp=cv.prioridad(pacientes)
    elif op==3: 
        pp=cv.prioridad(pacientes)
        cd=cv.citas(pp)
    elif op==4: 
        cv.busqueda(pp,cd)  #Buscar un paciente en concreto
    elif op==5:
        print("======================================================")
        print("Cerrando programa, gracias por su consulta") 
        print("======================================================")
        flag=2
    else:
        print("Error!!, opción no valida, intente de nuevo\n\n")

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
