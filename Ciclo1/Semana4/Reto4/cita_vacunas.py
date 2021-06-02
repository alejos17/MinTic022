""" Reto 4 Citas para Vacunacion  #
    Alejandro Tamayo
    Mayo 29-2021 """

# Definición de Funciones (Dividir)
import datetime as dt
from datetime import datetime, timedelta
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
#Funcion para llenar de datos las listas y probar funcionalidad del programa rapido
def datos_ejemplo():    #40 personas y su etapas asignadas
    """ 
    Parameters
    ----------
    Returns
    -------
    a:lista
        Entrega una lista con 40 pacientes y etapas asignadas, para prueba rapida
    """
    a=[('Alex', 2), ('Carlos', 3), ('Ramiro', 1), ('Antonio', 4), ('Alejandro', 5), ('Sandra', 2), ('Carolina', 1), ('Catalina', 3), ('Gloria', 2), ('Jorge', 5), ('Niky', 5), ('Carla', 3), ('Eliseo', 2), ('Ruth', 4), ('Fernando', 5), ('Modesta', 3), ('Hilario', 1), ('Judith', 2), ('Karen', 4), ('Juan', 2), ('Cristobal', 1), ('Samuel', 3), ('Jana', 5), ('Hector', 5), ('Raimundo', 2), ('Vanesa', 1), ('Jose', 2), ('Marta', 4), ('Andrea', 5), ('Zaida', 2), ('Joana', 3), ('Federico', 5), ('Erica', 5), ('Adam', 4), ('Gracia', 5), ('Julia', 3), ('Karina', 5), ('Lidia', 3), ('Benito', 1), ('Natalia', 5)]
    return a

#Funcion para solicitar datos de los pacientes manualmente
#El indice es la clave para concatenar el nombre del paciente con su etapa
def actualizando():
    """ 
    Parameters
    ----------
    Returns
    -------
    pacientes:lista
        Entrega una lista con los pacientes digitados manualmente, tanto su nombre como su etapa asignada
    """
    pacientes=[]
    i=1   #Bandera para entrar en el bucle
    while i==1:
        print("=======================================================")
        pacientes.append(ingreso_paciente())  #Va agregando nombres de pacientes en lista
        #etapas.append(ingreso_etapa())  #Va agregando la etapa del paciente en lista
        print(" ")
        i=int(input("Desea agregar otro paciente?: 1.Si  2.No: "))
        #Condicion para indicar el maximo de personas que se pueden registrar(Ej:40)
        if len(pacientes)>=40:
            print("Capacidad de pacientes excedida")
            break
    return pacientes

#Funcion para ingreso de Nombres de pacientes
def ingreso_paciente():
    """ 
    Parameters
    ----------
    Returns
    -------
    nombre, etapa:string, int
        Pide datos string para nombre y entero para la etapa
    """
    print(" \n")
    nombre=input("Por favor ingrese el nombre del paciente: ")
    etapa=int(input("Cual etapa fue asignada a este paciente?: "))
    return nombre, etapa

#Funcion para organizar las listas por prioridad segun su etapa
def prioridad(pacientes):
    """ 
    Parameters
    ----------
    pacientes:lista
        Entra la lista de pacientes y etapas
    Returns
    -------
    pp:Lista
        Entrega la lista de pacientes y etapas pero ordenada por etapa de 1 a 5
    """
    print(" \n")
    #print("La lista de pacientes es: ",pacientes)
    #Funcion lambda para ordenar la lista por index 1, osea etapa.
    pp=sorted(pacientes, key=lambda x: x[1])
    print("La lista de pacientes priorizada es: \n")
    print(pp)
    print("\n")
    return pp

#Funcion para buscar un paciente en la lista
def busqueda(pp,cd):
    """ 
    Parameters
    ----------
    pp,cd:Listas
        Entra la lista priorizada de pacientes y las citas disponibles asignadas
        No retorna valor, solo imprime por pantalla    
    """
    print(" \n")
    b=input("Indique el paciente a buscar?: ").capitalize()  #Entrada de paciente a buscar, aunque se escriba en minuscula
    
    #For para Buscar pacientes y su etapa
    for x in range (len(pp)):    #Recorrido Lista
        if b==pp[x][0]:         #Busqueda del paciente index 0
            a=pp[x][0]          #Si lo encuentra lo guarda aparte
            #Convertir de nuevo la fecha en String
            f=str(cd[x][2])+"/"+str(cd[x][1])+"/"+str(cd[x][0])
            #Convertir de nuevo la hora en String
            h=str(cd[x][3])+":"+str(cd[x][4])
            #Sacar el día de la semana con el metodo weekday()
            d=str(cd[x][5])
            #Condicionar para sacar le mensaje
            if d=="0": d="Lunes"
            elif d=="1": d="Martes"
            elif d=="2": d="Miércoles"
            elif d=="3": d="Jueves"
            elif d=="4": d="Viernes"
            elif d=="5": d="Sábado"
            elif d=="6": d="Domingo"
            print(" \n")
            print("================================================================")
            print("Paciente encontrado\n")
            print("Nombre: ",a)
            #print("Posicion: ", x)  #Toma el indice del registro
            print("Etapa de",a,"asignada es:",pp[x][1])   #Busca en etapas index 1 
            print("La cita se asigno para el día ",d," ",f," a las: ",h, " horas")
            print("================================================================")
    print(" \n")

def citas(pp):
    """ 
    Parameters
    ----------
    pp:Lista
        Entra la lista priorizada de pacientes
    Returns
    -------
    citasdisponibles:Lista
        Entrega una lista con las fechas y horas disponibles y las relaciona con la lista pp de usuarios, concatena por orden para indicar la cita del usuario
    """
    citasdisponibles=[]
    fecha_inicio="25/5/2021"
    fecha_ini=datetime.strptime(fecha_inicio, "%d/%m/%Y")
    hora_ini=dt.datetime(fecha_ini.year,fecha_ini.month,fecha_ini.day,10,0)
    hora_fin=dt.datetime(fecha_ini.year,fecha_ini.month,fecha_ini.day,12,0)
    hora_cita=hora_ini
    
    print(" \n")
    print("====================================================")
    print("*** Listado de citas por orden de Etapa asignada ***")
    print("====================================================")

    #Recorrer cada paciente de la lista priorizada
    for x in range (len(pp)):
        #print(pp[x][0])
        citasdisponibles.append((hora_cita.year,hora_cita.month,hora_cita.day,hora_cita.hour,hora_cita.minute,hora_cita.weekday()))
        
        #TODO hay que verificar porque toma la cita de las 12 si es menos
        if hora_cita.hour<12 :   
            hora_cita=hora_cita + dt.timedelta(minutes=20)
        else:
            hora_cita=hora_cita.replace(hour=10)
            hora_cita=hora_cita.replace(minute=0)
            hora_cita=hora_cita + dt.timedelta(days=1)
            
        #print(citasdisponibles)
        #Convertir de nuevo la fecha en String
        f=str(citasdisponibles[x][2])+"/"+str(citasdisponibles[x][1])+"/"+str(citasdisponibles[x][0])
        #Convertir de nuevo la hora en String
        h=str(citasdisponibles[x][3])+":"+str(citasdisponibles[x][4])
        #Sacar el día de la semana con el metodo weekday()
        d=str(citasdisponibles[x][5])
        #Condicionar para sacar le mensaje
        if d=="0": d="Lunes"
        elif d=="1": d="Martes"
        elif d=="2": d="Miércoles"
        elif d=="3": d="Jueves"
        elif d=="4": d="Viernes"
        elif d=="5": d="Sábado"
        elif d=="6": d="Domingo"

        print(pp[x][0]," Etapa: ",pp[x][1],"para el día: ",d," ",f," a las: ",h, " horas")
    
    return citasdisponibles
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias