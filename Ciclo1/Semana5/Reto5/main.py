from collections import namedtuple

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
    pacientes=namedtuple('Pacientes',['id','nombre','apellido','etapa','fecha_nac','edad','fecha_cita','hora_cita','vacuna'])
    
    vacunas=['Pfizer','AstrazZeneca','Moderna','Sinovac']
    
    lista_pacientes=[Pacientes(id='16078823', nombre='Alejandro', apellido='Tamayo', etapa='5', fecha_nac='17/02/1984', edad=0, fecha_cita='25/05/2021', hora_cita='10:00', vacuna='Sinovac'), Pacientes(id='1013597214', nombre='Sandra', apellido='Pachon', etapa='3', fecha_nac='15/06/1988', edad=0, fecha_cita='27/05/2021', hora_cita='10:40', vacuna='Moderna')]
    
    return lista_pacientes

def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 5")
    print("Vacunas:\n")
    print("1. Solicitud datos")
    print("2. Listar Datos")
    print("3. Correr programa")
    print("4. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: 
        lista_pacientes=solicitud_datos()
    elif op==2: listar_datos(lista_pacientes)
    elif op==3: exit()
    else: print("Opción no valida, intente de nuevo")


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

2. Guardar tupla tipo paciente con los datos
3. Guardar una lista de pacientes con la tupla
4. contar el total de pacientes en la lista para el primer reporte
5. sacar los datos por cada tipo de vacuna
6. armar nuevas tuplas por tipo de vacuna
7. armar listas por vacuna.
8. sacar reporte por tipo de vacuna
"""