""" Reto 6 Informes de Vacunacion #
    Tu nombre aquí
    Junio XX-XX """

# Definición de Funciones (Dividir)
#-*- coding: utf-8 -*-
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
    print("*************************************************************")
    print("Apertura de Archivo: Data1.csv +++++++++")
    with open('/home/alejos17/Documents/code_alejos17/MinTic022/Ciclo1/Semana6/Reto6/Data1.csv',encoding='utf-8-sig') as File:
            reader = csv.reader(File)
            print("Leyendo lineas de archivo: (Espere....)")
            i=0
            for row in reader:
                p=pacientes(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40])
                lista_pacientes.append(p)
    File.close()
    print("*************************************************************")
    print("Archivo Data1.csv cargado")
    print("Pacientes cargados: 1000")
    print("*************************************************************")
    return lista_pacientes

def graficos_gral(lista_pacientes):
    flag=1
    while flag==1:
        print("=======================================")
        print("++++++  Generar Grafico General ++++++")
        print("=======================================")
        print("1. Grafico por Ciudad")
        print("2. Grafico por Tipo de Vacuna")
        print("3. Grafico por Etapa")
        print("4. Grafico por Genero")
        print("5. Grafico por Fecha de Vacunación")
        print("6. Grafico por Hora de Vacunación")
        print("7. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        if a==1: b="ciudad"
        elif a==2: b="vacuna"
        elif a==3: b="etapa"        
        elif a==4: b="genero"
        elif a==5: b="fecha_cita"
        elif a==6: b="hora_cita"
        elif a==7: break
        else: print("Opción no válida, intente de nuevo")

        nombres,datos,dic=calculo_datos(lista_pacientes,b)
        if a==3:
            for x in range(len(nombres)):
                nombres[x]=b+" "+str(nombres[x])
        
        graficador(nombres,datos,b)
    return None

def graficos_esp(lista_pacientes):
    flag=1
    while flag==1:
        print("=======================================")
        print("+++++  Generar Grafico Específico +++++")
        print("=======================================")
        print("--- Seleccione la variable inicial ---")
        print("1. Ciudad")
        print("2. Tipo de Vacuna")
        print("3. Etapa")
        print("4. Genero")
        print("5. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        print("=======================================")
        print("--- Seleccione la segunda variable ---")
        print("1. Ciudad")
        print("2. Tipo de Vacuna")
        print("3. Etapa")
        print("4. Genero")
        print("5. Fecha de Vacunación")
        print("6. Volver Atrás")
        print("---------------------------------------")
        a2=int(input("Escriba la opcion: "))
        if a==a2:
            print("Ha seleccionado la misma variable ambas veces, es inválido, intente de nuevo")
            exit()
        if a==1:
            b="ciudad"
            print("***************************************************")
            z=input("Indique el Nombre de la Ciudad: ").capitalize()
            print("***************************************************")
            if a2==2: b2="vacuna"
            elif a2==3: b2="etapa" 
            elif a2==4: b2="genero"
            elif a2==5: b2="fecha_cita"
            elif a2==6: break
        elif a==2: 
            b="vacuna"
            print("***************************************************")
            z=input("Indique el Nombre de la Vacuna: ").capitalize()
            print("***************************************************")
            if a2==1: b2="ciudad"
            elif a2==3: b2="etapa" 
            elif a2==4: b2="genero"
            elif a2==5: b2="fecha_cita"
            elif a2==6: break
        elif a==3: 
            b="etapa"
            print("***************************************************")
            z=input("Indique la etapa: ").capitalize()
            print("***************************************************")        
            if a2==1: b2="ciudad"
            elif a2==2: b2="vacuna" 
            elif a2==4: b2="genero"
            elif a2==5: b2="fecha_cita"
            elif a2==6: break
        elif a==4:  #TODO No funciona la grafica genero x cualquiera(revisar)
            b="genero"
            print("***************************************************")
            z=input("Indique el genero (masculino / femenino): ").capitalize()
            print("***************************************************")
            if a2==1: b2="ciudad"
            elif a2==2: b2="vacuna" 
            elif a2==3: b2="etapa"
            elif a2==5: b2="fecha_cita"
            elif a2==6: break
        elif a==5: break
        else: print("Opción no válida, intente de nuevo")

        nombres,datos,dic=calculo_datos_doble(lista_pacientes,b,b2,z)
        if a2==3:
            for x in range(len(nombres)):
                nombres[x]="Etapa "+str(nombres[x])
        if a==3:
            z="Etapa "+str(z)

        graficador(nombres,datos,z)
    return None


def calculo_datos(lista_pacientes,b):
    lista=[]
    for x in range(len(lista_pacientes)):
        lista.append(getattr(lista_pacientes[x], b))
        cantidad=Counter(lista)

    #Se ordena el diccionario generado por Counter de
    #forma ascendente
    cantidad_ord = dict(sorted(cantidad.items()))
    nombres=cantidad_ord.keys()
    datos=cantidad_ord.values()
    nombres=list(nombres)
    return nombres,datos,cantidad_ord

def calculo_datos_doble(lista_pacientes,b,b2,z):
    listab=[]
    listab2=[]
    for x in range(len(lista_pacientes)):
        if z==getattr(lista_pacientes[x], b):
            listab.append(getattr(lista_pacientes[x], b))
            listab2.append(getattr(lista_pacientes[x], b2))
            cantidad=Counter(listab2)
    
    #Se ordena el diccionario generado por Counter de
    #forma ascendente
    #print("Debe aparecer solo una ciudad")
    #print(len(cantidad))
    print(listab)
    print("********************************************")
    print(listab2)
    cantidad_ord = dict(sorted(cantidad.items()))
    nombres=cantidad_ord.keys()
    datos=cantidad_ord.values()
    nombres=list(nombres)
    return nombres,datos,cantidad_ord

def graficador(nombres,datos,b):
    #Grafica Vertical para etapa, vacuna y genero, pocos datos
    #Sacado de: https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
    if b=="etapa" or b=="vacuna" or b=="genero":
        fig = plt.figure(u'Gráfica de barras') # Figure
        ax = fig.add_subplot(111) # Axes
        xx = range(len(datos))
        ax.bar(xx, datos, width=0.8, align='center')
        ax.set_xticks(xx)
        ax.set_xticklabels(nombres)
    else:
    #Grafica Horizontal para mostrar bien cuando son muchos datos
    #sacado de: https://matplotlib.org/stable/gallery/https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-pylines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
        plt.rcdefaults()
        fig, ax = plt.subplots()
        y_pos = np.arange(len(nombres))
        error = np.random.rand(len(nombres))
        ax.barh(y_pos, datos, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(nombres)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Cantidad de Personas')
        ax.set_title('Grafica por '+b)
        
    plt.show()
    return None

def listar_datos(lista_pacientes):
    flag=1
    while flag==1:
        print("=======================================")
        print("+++++++++  Listado de Datos ++++++++++")
        print("=======================================")
        print("1. por Ciudad")
        print("2. por Tipo de Vacuna")
        print("3. por Etapa")
        print("4. por Genero")
        print("5. por Fecha de Vacunación")
        print("6. por Hora de Vacunación")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        if a==1: b="ciudad"
        elif a==2: b="vacuna"
        elif a==3: b="etapa"
        elif a==4: b="genero"
        elif a==5: b="fecha_cita"
        elif a==6: b="hora_cita"
        elif a==7: break
        else: print("Opción no válida, intente de nuevo")

        nombres,datos,dic=calculo_datos(lista_pacientes,b)
        dic2=dic.items()  #crea una tupla con clave y valor para print bonito
        print("---------------------------------------")
        print("++++ Lista por ",b," ++++")
        print("| ",b," | Cantidad de personas |")
        print("---------------------------------------")
        for elemento in dic2:
            print(elemento)
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