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
    flag=1
    opv=0
    while flag==1:
        cedula=input("Digite su numero de cedula: ")
        nombre=input("Digite su nombre: ")
        apellido=input("Digite su apellido: ")
        etapa=input("Digite la etapa asignada del paciente: ")
        fecha_nac=input("Digite su fecha de nacimiento: (dd/mm(yy)")
        edad=0
        fecha_cita=input("Cual fue el día de aplicación de la vacuna?: (dd/mm/yy)")
        hora_cita=input("Cual fue la hora de la cita?: (hh:mm)")
        
        flag=1
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
        
        p=pacientes(cedula,nombre,apellido,etapa,fecha_nac,edad,fecha_cita,hora_cita,vacuna)

        lista_pacientes.append(p)
        
        flag=int(input("Desea agregar otro paciente?: 1.Si  2.No: "))
        if flag>2 or flag <=0:
            print("opción invalida, repita de nuevo...")
            flag=1

        print(lista_pacientes)
    #TODO Calcular la edad y tener el valor en int
    return lista_pacientes

def listar_datos(lista_pacientes):
    for element in range(len(lista_pacientes)):
        print(lista_pacientes[element])
        print("-----------------------------------------")
    return

def datos_ejemplo():
    lid=['16078823','1013597214','70119227','30290206']
    lnombres=['Alejandro','Sandra','Jorge','Gloria']
    lapellido=['Tamayo','Pachon','Tamayo','Zuluaga']
    letapa=['5','3','2','2']
    lfecha_nac=['17/02/1984','15/06/1988','17/01/1984','14/12/1963']
    ledad=['37','34','65','60']
    lfecha_cita=['25/05/2021','27/05/2021','26/05/2021','27/05/2021']
    lhora_cita=['10:00','10:40','11:40','10:20']
    lvacuna=['Pfizer','Sinovac','Sinovac','Pfizer']

    for i in range(len(lid)):
        p=pacientes(lid[i],lnombres[i],lapellido[i],letapa[i],lfecha_nac[i],ledad[i],lfecha_cita[i],lhora_cita[i],lvacuna[i])
        lista_pacientes.append(p)
    
    print("Datos cargados: ")
    print(lista_pacientes)

    return lista_pacientes

def busqueda(lista_pacientes):
    lista_busqueda=[]
    flag=1
    while flag==1:
        print("Desea buscar por?: ")
        print("1. Documento")
        print("2. Nombre de Paciente")
        print("3. Apellido de Paciente")
        print("4. Tipo de Vacuna")
        print("5. Etapa de Vacunación")
        opv=int(input("Seleccione: "))
        if opv==1: 
            b=input("Indique el documento a buscar: ")
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].id:
                    print(lista_pacientes[x].id)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==2: 
            b=input("Indique el Nombre a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].nombre:
                    print(lista_pacientes[x].nombre)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==3: 
            b=input("Indique el Apellido a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].apellido:
                    print(lista_pacientes[x].apellido)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==4: 
            b=input("Indique el Tipo de Vacuna a buscar: ").capitalize()
            for x in range(len(lista_pacientes)):
                if b==lista_pacientes[x].vacuna:
                    print(lista_pacientes[x].vacuna)
                    p=pacientes(lista_pacientes[x].id,lista_pacientes[x].nombre,lista_pacientes[x].apellido,lista_pacientes[x].etapa,lista_pacientes[x].fecha_nac,lista_pacientes[x].edad,lista_pacientes[x].fecha_cita,lista_pacientes[x].hora_cita,lista_pacientes[x].vacuna)
                    lista_busqueda.append(p)
            flag=2
        elif opv==5: 
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