""" Reto 5 Vacunacion para Todos #
    Alejandro Tamayo
    Junio 5-2021 """

# Definición de Funciones (Dividir)
from collections import namedtuple
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
pacientes=namedtuple('Pacientes',['id','nombre','apellido','etapa','fecha_nac','edad','fecha_cita','hora_cita','vacuna'])
vacunas=['Pfizer','AstrazZeneca','Moderna','Sinovac']
lista_pacientes=[]

def solicitud_datos():
    """ 
    Parameters
    ----------
    Returns
    -------
    lista_pacientes:[(namedtuple)]
        Una lista con una tupla de formato pacientes con los datos generales del paciente
    """
    flag=1          #Bandera para entrar en bucle
    opv=0           #Variable para opción en el menu de usuario
    while flag==1:
        cedula=input("Digite su numero de cedula: ")
        nombre=input("Digite su nombre: ")
        apellido=input("Digite su apellido: ")
        etapa=input("Digite la etapa asignada del paciente: ")
        fecha_nac=input("Digite su fecha de nacimiento: (dd/mm(yy)")
        edad=0
        fecha_cita=input("Cual fue el día de aplicación de la vacuna?: (dd/mm/yy)")
        hora_cita=input("Cual fue la hora de la cita?: (hh:mm)")
        
        flag=1      #Bandera para entrar a bucle de selección de vacuna
        while flag==1:
            print("Que vacuna le fue aplicada?: ")
            print("1. Pfizer")
            print("2. AstraZeneca")
            print("3. Moderna")
            print("4. Sinovac")
            opv=int(input("Seleccione: "))
            if opv==1: 
                vacuna=vacunas[0]
                flag=2
            elif opv==2: 
                vacuna=vacunas[1]
                flag=2
            elif opv==3: 
                vacuna=vacunas[2]
                flag=2
            elif opv==4: 
                vacuna=vacunas[3]
                flag=2
            else: print("opcion incorreta")
        
        #Se guarda la tupla con todos los datos recopilados del paciente
        p=pacientes(cedula,nombre,apellido,etapa,fecha_nac,edad,fecha_cita,hora_cita,vacuna)

        #Se anexa la tupla a la lista
        lista_pacientes.append(p)
        
        #Solicitud por pantalla para agregar otro paciente en un if.
        flag=int(input("Desea agregar otro paciente?: 1.Si  2.No: "))
        if flag>2 or flag <=0:
            print("opción invalida, repita de nuevo...")
            flag=1

        print(lista_pacientes)
    #TODO Calcular la edad y tener el valor en int
    return lista_pacientes

def listar_datos(lista_pacientes):
    """ 
    Parameters
    ----------
    lista_pacientes:NamedTuple
        Lista con las tuplas por cada paciente
    Return
    -------
        No retorna valores, imprime en pantalla del usuario
    """
    #Creación de listas por cada dato del paciente de nuevo para poder sacar estadisticas por cantidades
    #Ya sea cantidad de personas, por tipo de vacunas
    lid=[]  
    lnombres=[]
    lapellido=[]
    letapa=[]
    lfecha_nac=[]
    ledad=[]
    lfecha_cita=[]
    lhora_cita=[]
    lvacuna=[]
    lvacunap=[]
    lvacunaa=[]
    lvacunam=[]
    lvacunasi=[]
    letapa1=[]
    letapa2=[]
    letapa3=[]
    letapa4=[]
    letapa5=[]
    
    #Ciclo para guardar datos de la lista de pacientes en listas independientes para conteo
    for x in range(len(lista_pacientes)):
        lid.append(lista_pacientes[x].id)
        lnombres.append(lista_pacientes[x].nombre)
        lapellido.append(lista_pacientes[x].apellido)
        letapa.append(lista_pacientes[x].etapa)
        lfecha_nac.append(lista_pacientes[x].fecha_nac)
        ledad.append(lista_pacientes[x].edad)
        lfecha_cita.append(lista_pacientes[x].fecha_cita)
        lhora_cita.append(lista_pacientes[x].hora_cita)
        lvacuna.append(lista_pacientes[x].vacuna)
    
    #Listar por marca de vacuna para desplegar información de vacunados por cada una de las 
    #marca de vacuna
    for x in range(len(lvacuna)):
        if lvacuna[x]=="Pfizer":
            lvacunap.append(lvacuna[x])
        elif lvacuna[x]=="AstraZeneca":
            lvacunaa.append(lvacuna[x])
        elif lvacuna[x]=="Moderna":
            lvacunam.append(lvacuna[x])
        elif lvacuna[x]=="Sinovac":
            lvacunasi.append(lvacuna[x])

    #Listar por etapa de vacunación para desplegar información de vacunados
    for x in range(len(letapa)):
        if letapa[x]=="1":
            letapa1.append(letapa[x])
        elif letapa[x]=="2":
            letapa2.append(letapa[x])
        elif letapa[x]=="3":
            letapa3.append(letapa[x])
        elif letapa[x]=="4":
            letapa4.append(letapa[x])
        elif letapa[x]=="5":
            letapa5.append(letapa[x])

    #Mensajes en Pantalla
    print("\n")
    print("Se tienen registrados: ",len(lista_pacientes),"pacientes")
    print("Pesonas vacunadas con Pfizer: ",len(lvacunap))
    print("Pesonas vacunadas con AstraZeneca: ",len(lvacunaa))
    print("Pesonas vacunadas con Moderna: ",len(lvacunam))
    print("Pesonas vacunadas con Sinovac: ",len(lvacunasi))
    print("")
    print("Personas Vacunadas de Etapa 1: ",len(letapa1))
    print("Personas Vacunadas de Etapa 2: ",len(letapa2))
    print("Personas Vacunadas de Etapa 3: ",len(letapa3))
    print("Personas Vacunadas de Etapa 4: ",len(letapa4))
    print("Personas Vacunadas de Etapa 5: ",len(letapa5))
    print("\n")

    for element in range(len(lista_pacientes)):
        print(lista_pacientes[element])
        print("-----------------------------------------")
    return

def datos_ejemplo():
    """ 
    Parameters
    ----------
    Returns
    -------
    lista_pacientes:[(namedtuple)]
        Se genera la lista de pacientes con datos de ejemplo anexados para pruebas rápidas
    """
    lid=['16078823','1013597214','70119227','30290206']
    lnombres=['Alejandro','Sandra','Jorge','Gloria']
    lapellido=['Tamayo','Pachon','Tamayo','Zuluaga']
    letapa=['5','3','2','2']
    lfecha_nac=['17/02/1984','15/06/1988','17/01/1984','14/12/1963']
    ledad=['37','34','65','60']
    lfecha_cita=['25/05/2021','27/05/2021','26/05/2021','27/05/2021']
    lhora_cita=['10:00','10:40','11:40','10:20']
    lvacuna=['Pfizer','Sinovac','Sinovac','Pfizer']

    #Recorrido por una de las listas para crear la tupla y anexar a la lista
    for i in range(len(lid)):
        p=pacientes(lid[i],lnombres[i],lapellido[i],letapa[i],lfecha_nac[i],ledad[i],lfecha_cita[i],lhora_cita[i],lvacuna[i])
        lista_pacientes.append(p)
    
    print("Datos cargados: ")
    print(lista_pacientes)

    return lista_pacientes

def busqueda(lista_pacientes):
    """ 
    Parameters
    ----------
    lista_pacientes:NamedTuple
        Lista de tuplas con la información de cada paciente
    Returns
    -------
        No retorna valores, imprime en pantalla del usuario
    """
    #Lista para guardar la tupla del valor buscado y desplegar información del paciente buscado
    lista_busqueda=[]
    flag=1
    while flag==1:          #Se crea menú para buscar por diferentes criterios
        print("Desea buscar por?: ")
        print("1. Documento")
        print("2. Nombre de Paciente")
        print("3. Apellido de Paciente")
        print("4. Tipo de Vacuna")
        print("5. Etapa de Vacunación")
        opv=int(input("Seleccione: "))
        if opv==1: 
            b=input("Indique el documento a buscar: ")  #Busqueda por documento
            for x in range(len(lista_pacientes)):   
                if b==lista_pacientes[x].id:        #Si se encuentra documento
                    print(lista_pacientes[x].id)    #Se graba toda la info de ese paciente en una tupla y se agrega a lista 
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==2:            #Busqueda por nombre
            b=input("Indique el Nombre a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].nombre:
                    print(lista_pacientes[x].nombre)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==3:            #Busqueda por apellido
            b=input("Indique el Apellido a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].apellido:
                    print(lista_pacientes[x].apellido)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==4:            #Busqueda por tipo de vacuna
            b=input("Indique el Tipo de Vacuna a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].vacuna:
                    print(lista_pacientes[x].vacuna)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==5:            #Busqueda por etapa de vacunación
            b=input("Indique la etapa de Vacunación: ")
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].etapa:
                    print(lista_pacientes[x].etapa)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2            
        else: print("opcion incorreta")
    
    print("La busqueda es: ")
    print("Pacientes encontrados: ",len(lista_busqueda))
    for i in range(len(lista_busqueda)):
        print(lista_busqueda[i])
    return



#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias