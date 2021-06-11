""" Reto 6 Informes de Vacunacion #
    Tu nombre aquí
    Junio XX-XX """

# Definición de Funciones (Dividir)
import csv
from collections import namedtuple, Counter
import matplotlib.pyplot as plt
import numpy as np

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
pacientes=namedtuple('Pacientes',['genero','nombre','apellido','direccion','ciudad','email','telefono','fecha_nac','edad','id','sangre','ts','th','th1','teb','td','tir','tvih','tc','tb','te','ta','to','tls','tpl','tp','tpol','tam','tre','tbc','tcr','tdc','tca','tba','tpt','tav','tec','etapa','fecha_cita','hora_cita','vacuna'])
lista_pacientes=[]

def leer_archivo():
    with open('/home/alejos17/Documents/code_alejos17/MinTic022/Ciclo1/Semana6/Reto6/Data1.csv') as File:
            reader = csv.reader(File)
            for row in reader:
                p=pacientes(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40])
                lista_pacientes.append(p)
    return lista_pacientes

#TODO ya lo hace grafico_general
def grafico_etapas(lista_pacientes):
    e1=[]
    e2=[]
    e3=[]
    e4=[]
    e5=[]
    for x in range(len(lista_pacientes)):
        if lista_pacientes[x].etapa=="1":
            e1.append(lista_pacientes[x].etapa)
        if lista_pacientes[x].etapa=="2":
            e2.append(lista_pacientes[x].etapa)
        if lista_pacientes[x].etapa=="3":
            e3.append(lista_pacientes[x].etapa)
        if lista_pacientes[x].etapa=="4":
            e4.append(lista_pacientes[x].etapa)
        if lista_pacientes[x].etapa=="5":
            e5.append(lista_pacientes[x].etapa)        

    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = ['Etapa 1','Etapa 2','Etapa 3','Etapa 4','Etapa 5']
    datos = [len(e1),len(e2),len(e3),len(e4),len(e5)]
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.show()
    return None

#TODO BORRAR YA lo hace grafico_general
def grafico_vacunas(lista_pacientes):
    pfizer=[]
    astra=[]
    moderna=[]
    sinovac=[]
    for x in range(len(lista_pacientes)):
        if lista_pacientes[x].vacuna=="Pfizer":
            pfizer.append(lista_pacientes[x].vacuna)
        if lista_pacientes[x].vacuna=="AstraZeneca":
            astra.append(lista_pacientes[x].vacuna)
        if lista_pacientes[x].vacuna=="Moderna":
            moderna.append(lista_pacientes[x].vacuna)
        if lista_pacientes[x].vacuna=="Sinovac":
            sinovac.append(lista_pacientes[x].vacuna)
        
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = ['Pfizer','AstraZeneca','Moderna','Sinovac']
    datos = [len(pfizer),len(astra),len(moderna),len(sinovac)]
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.show()
    return None

def grafico_general(lista_pacientes):
    a=int(input("Escriba la opcion: "))
    if a==1:
        b="ciudad"
    elif a==2:
        b="vacuna"
    elif a==3:
        b="etapa"    

    lista=[]
    for x in range(len(lista_pacientes)):
        lista.append(getattr(lista_pacientes[x], b))
        cantidad=Counter(lista)
        
    nombres=cantidad.keys()
    datos=cantidad.values()
    
    print(cantidad)
    print(len(cantidad))
    print(nombres)
    print(datos)

    graficador(nombres,datos)

    return

def graficador(nombres,datos):
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.show()
    return None




#TODO Revisar si esto se puede utilizar.

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

    for element in range(len(lista_pacientes)):
        print(lista_pacientes[element])
        print("-----------------------------------------")
    
    #Mensajes en Pantalla
    print("\n")
    print("Se tienen registrados: ",len(lista_pacientes),"pacientes\n")
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
    
    return


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