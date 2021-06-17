""" Reto 6 Informes de Vacunacion #
    Alejandro Tamayo
    Junio 13-2021 """

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

#IV_06_RS_02
def leer_archivo():
    """ 
    Parameters
    ----------
    Returns
    -------
    lista_pacientes: Lista de Tuplas
        Lista de tuplas namedtuples tipo Pacientes, con los datos de cada paciente
    """
    print("*************************************************************")
    print("Apertura de Archivo: Data1.csv +++++++++")
    #Apertura del archivo con la fucion with open del modulo CSV
    #Este lee los datos separados por comas, con formato UTF8
    with open('/home/alejos17/Documents/code_alejos17/MinTic022/Ciclo1/Semana6/Reto6/Data1.csv',encoding='utf-8-sig') as File:  #Apertura del archivo
            reader = csv.reader(File)  #Funcion de lectura del archivo
            print("Leyendo lineas de archivo: (Espere....)")  #Mensaje al usuario
            #Recorrido por cada linea del archivo que es la información de un paciente
            #con todos sus datos, se guardan en una tupla tipo Paciente, definida arriba
            #En este archivo son 40 datos por paciente se guarda cada posicion de la fila
            #de 0 a 40 en una tupla y luego se anexa a una lista (lista_pacientes)
            for row in reader:
                p=pacientes(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40])
                lista_pacientes.append(p)  #Se anexa a la lista de tuplas
    File.close()  #Se cierra el archivo
    #Mensaje al usuario
    print("*************************************************************")
    print("Archivo Data1.csv cargado")
    print("Pacientes cargados: 1000")
    print("*************************************************************")
    return lista_pacientes

#IV_06_RS_03
def graficos_gral(lista_pacientes):
    """ 
    Parameters
    ----------
    lista_pacientes: Lista de Tuplas
        Información de los pacientes 
    Returns
    -------
        Imprime en Pantalla la gráfica solicitada
    """
    flag=1 #Bandera para entrar en Bucle del menú
    while flag==1:
        print("=======================================")
        print("++++++  Generar Grafico General ++++++")
        print("=======================================")
        print("1. Ciudades")
        print("2. Tipo de Vacuna")
        print("3. Etapa")
        print("4. Genero")
        print("5. Tipo Sanguineo")
        print("6. Grafico por Fecha de Vacunación")
        print("7. Grafico por Hora de Vacunación")
        print("8. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        #Según lo seleccionado por el usuario, se carga en la variable b el dato que se requiere graficar
        if a==1: b="ciudad"
        elif a==2: b="vacuna"
        elif a==3: b="etapa"        
        elif a==4: b="genero"
        elif a==5: b="sangre"
        elif a==6: b="fecha_cita"
        elif a==7: b="hora_cita"
        elif a==8: break
        else: print("Opción no válida, intente de nuevo")
        
        #Se envia la lista de pacientes y la variable b a "calculo_datos" para sacar la información en
        #relación a "b" solamente y devuelve:  nombres: descripción de los valores  y datos: los
        #valores en si en forma de entero para el tamaño de las barras de la grafica
        #"dic" no se usa en esta funcion, solo el listar_datos()
        nombres,datos,dic=calculo_datos(lista_pacientes,b)
        
        #Si la opción selecciona es por "Etapa", se agrega a los nombres para graficar la palabra
        #"Etapa", ya que en la tabla el valor es 1 o 2 o 3 etc.  Esto es solamente estetico al 
        #momento de gráficar.
        if a==3:
            for x in range(len(nombres)):
                nombres[x]=b+" "+str(nombres[x])
        
        #Se envian los datos devueltos por "calculo_datos" a la función graficador para desplegar
        #la imagen en pantalla.
        graficador(nombres,datos,b)
    return None

#IV_06_RS_04
def graficos_esp(lista_pacientes):
    """ 
    Parameters
    ----------
    lista_pacientes: Lista de Tuplas
        Información de los pacientes 
    Returns
    -------
        Imprime en Pantalla la gráfica solicitada
    """
    #En los graficos especificos se pueden enviar 2 varibles para generar graficos de tipo
    #"Grafico de Etapas en la ciudad de Manizales"
    #"Grafico de Genero por Tipo de Vacuna"
    #Se puede graficar casos más especificos
    flag=1   #Bandera para entrar en el bucle del menú
    while flag==1:
        #Se le pregunta al usuario la primer variable
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
        #Se le pregunta al usuario por la segunda variable
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
        #Primera condicion valida que el usuario no seleccione la misma variable en ambos casos
        #Se despliega mensaje de error
        if a==a2:
            print("Ha seleccionado la misma variable ambas veces, es inválido, intente de nuevo")
            exit()  #Cierra el programa 
        if a==1:   #Se asigna la primera variable en "b"  y la segunda variable en "b2 y se captura z el valor de "b"
            b="ciudad"  #Para que la funcion "calculo_datos_dobles", sepa que valor buscar y en que clave buscar.
            print("***************************************************")
            z=input("Indique el Nombre de la Ciudad: ").capitalize()   #Se puede escribir en mayuculas o minusculas
            print("***************************************************")
            if a2==2: b2="vacuna"     #Si se selecciona ej: asigna b="ciudad" y b2="Vacuna"
            elif a2==3: b2="etapa"    #Se pregunta "z" en relación a "b", si es ciudad, cual ciudad es la que se va
            elif a2==4: b2="genero"   #a consultar y todo esto se envia a "calculo_datos_dobles"
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
        elif a==4:  
            b="genero"
            print("***************************************************")
            z=input("Indique el genero (m: masculino / f: femenino): ")
            print("***************************************************")
            f=1      #Bandera para entrar a un mini bucle en la seleccion de genero 
            while f==1:  #para que el usuario escriba m o f solamente en esta opción.
                if z=="m" or z=="f":
                    if a2==1: b2="ciudad"
                    elif a2==2: b2="vacuna" 
                    elif a2==3: b2="etapa"
                    elif a2==5: b2="fecha_cita"
                    elif a2==6: break
                    if z=="m": z="masculino"
                    elif z=="f": z="femenino"
                    f=2
                else: print("Opción no válida, intente de nuevo")
        elif a==5: break
        else: print("Opción no válida, intente de nuevo")
        
        #Se envia la lista de pacientes y las variables "b","b2" y "z" a "calculo_datos" para sacar la información
        #"z" en relación a "b" y "b2" en relacion a "z" y devuelve:  nombres: descripción de los valores  y datos: los
        #valores en si en forma de entero para el tamaño de las barras de la grafica
        #"dic" no se usa en esta funcion, solo el listar_datos()
        nombres,datos,dic=calculo_datos_doble(lista_pacientes,b,b2,z)
        
        #Si la opción selecciona es por "Etapa", se agrega a los nombres para graficar la palabra
        #"Etapa", ya que en la tabla el valor es 1 o 2 o 3 etc.  Esto es solamente estetico al 
        #momento de gráficar.
        if a2==3:
            for x in range(len(nombres)):
                nombres[x]="Etapa "+str(nombres[x])
        if a==3:
            z="Etapa "+str(z)

        #Se envian los datos devueltos por "calculo_datos_dobles" a la función graficador para desplegar
        #la imagen en pantalla.
        graficador(nombres,datos,z)
    return None

#IV_06_RS_05
def calculo_datos(lista_pacientes,b):
    """ 
    Parameters
    ----------
    lista_pacientes, b: lista de tuplas, string
        Entra la lista con todos los pacientes y el valor a buscar
    Returns
    -------
    nombres,datos: listas
        Lista nombres con descripciones de los valores
        Lista datos con los valores para las graficas
    """
    #Se crea lista para extracción de datos
    lista=[]

    #Se recorre la lista entera de los pacientes y se saca el valor según "b"
    for x in range(len(lista_pacientes)):
        lista.append(getattr(lista_pacientes[x], b))  #Se anexa el valor encontrado a lista
        cantidad=Counter(lista)  #Se realiza un Counter sobre esta para determinar la cantidad de valores encontrados

    #Se ordena el diccionario generado por Counter de
    #forma ascendente
    cantidad_ord = dict(sorted(cantidad.items()))
    #Se extraen las claves del diccionario al diccionario nombres
    nombres=cantidad_ord.keys()
    #Se extraen los valores del diccionario al diccionario datos
    datos=cantidad_ord.values()
    #Se convierte el diccionario nombres a lista, para poder editar y concatenar Strings facilmente
    nombres=list(nombres)
    return nombres,datos,cantidad_ord

#IV_06_RS_06
def calculo_datos_doble(lista_pacientes,b,b2,z):
    """ 
    Parameters
    ----------
    lista_pacientes, b, b2, z: lista de tuplas, string, string, string
        Entra la lista con todos los pacientes y el valor del indice a buscar
        El valor del segundo indice y el valor de "b" en la tabla
        Ej: (b="ciudad"  b2="Vacuna z="Manizales")
    Returns
    -------
    nombres,datos: listas
        Lista nombres con descripciones de los valores
        Lista datos con los valores para las graficas
    """
    #Se crean las listas para extracción de datos
    listab=[]
    listab2=[]

    #Se recorre la lista entera de los pacientes y se saca el valor según "z"
    for x in range(len(lista_pacientes)):
        if z==getattr(lista_pacientes[x], b):  #Si z esta en la clave "b" ej:(Si Manizales esta en ciudad)
            listab.append(getattr(lista_pacientes[x], b)) #Se agrega a la lista el valor de "b"
            listab2.append(getattr(lista_pacientes[x], b2)) #Se agrega a la lista el valor de "b2" Ej: "Vacunas"
            cantidad=Counter(listab2)  #Se realiza función Counter sobre los datos b2 para sacar cantidades Ej: Pfizer: 7
    
    #Se ordena el diccionario generado por Counter de
    #forma ascendente
    cantidad_ord = dict(sorted(cantidad.items()))
    #Se extraen las claves del diccionario al diccionario nombres
    nombres=cantidad_ord.keys()
    #Se extraen los valores del diccionario al diccionario datos
    datos=cantidad_ord.values()
    #Se convierte el diccionario nombres a lista, para poder editar y concatenar Strings facilmente
    nombres=list(nombres)
    return nombres,datos,cantidad_ord

#IV_06_RV_07
def graficador(nombres,datos,b):
    """ 
    Parameters
    ----------
    nombres, datos, b: lista, lista, string
        Entra la lista con nombres y el conteo en datos con un valor string para
        poner el titulo de la gráfica
    Returns
    -------
        Imprime en Pantalla la gráfica solicitada
        Para pocas opciones de datos, se utiliza grafica de barras vertical.
        Para muchas opciones de datos, como ciudades, se usa grafica de barra horizontal.
    """
    plt.style.use('seaborn')  #Aplicar estilo de gráfica de matplotlib.org
    #Grafica Vertical para etapa, vacuna y genero, pocos datos
    #Sacado de: https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
    if b=="etapa" or b=="vacuna" or b=="genero":
        fig, ax = plt.subplots() #Llamando Figura y Ejes
        x_pos = range(len(datos))  # Valores del eje X, la cantidad de datos encontrados
        ax.bar(x_pos, datos, align='center') #Barra vertical centradas: cantidad barras, valores, alineación.
        ax.set_xticks(x_pos)  #Asignar valores a las posiciones en eje X
        ax.set_xticklabels(nombres) 
        ax.set_ylabel('Cantidad de Personas') #Titulo del eje y
        ax.set_title('Grafica por '+b)  #Titulo de la gráfica
    else:
    #Grafica Horizontal para mostrar bien cuando son muchos datos
    #sacado de: https://matplotlib.org/stable/gallery/https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-pylines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
        fig, ax = plt.subplots() #Llamando Figura y Eje
        y_pos = range(len(nombres)) #Valores del eje Y, cantidad de datos encontrados
        ax.barh(y_pos, datos, align='center') #Barra horizontal centradas: cantidad de barras, valores, alineación.
        ax.set_yticks(y_pos) #Asignar valores a las posiciones en eje Y
        ax.set_yticklabels(nombres)
        ax.invert_yaxis()  #Invertir el eje Y para que la información salga en orden de arriba a abajo, no al revés, por comienzo en Y=0 del plano cartesiano.
        ax.set_xlabel('Cantidad de Personas') #Titulo del eje X
        ax.set_title('Grafica por '+b) # Titulo de la grafica
                
    plt.show()  #Imprimir grafico seleccionado en pantalla.
    return None

#IV_06_RS_08
def listar_datos(lista_pacientes):
    """ 
    Parameters
    ----------
    lista_pacientes: Lista de Tuplas
        Información de los pacientes 
    Returns
    -------
        Imprime en Pantalla la gráfica solicitada
    """
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

        ##Se envia la lista de pacientes y la variable b a "calculo_datos" para sacar la información en
        #relación a "b" solamente y devuelve:  dic: diccionario con nombres y valores para imprimir en pantalla
        #"nombres" y "datos" no se usan en esta funcion, ya que no grafica
        nombres,datos,dic=calculo_datos(lista_pacientes,b)
        dic2=dic.items()  #crea una tupla con clave y valor para print bonito
        #Mensaje en Pantalla
        print("---------------------------------------")
        print("++++ Lista por ",b," ++++")
        print("| ",b," | Cantidad de personas |")
        print("---------------------------------------")
        #Recorrido de diccionario para imprimir en pantalla
        for elemento in dic2:
            print(elemento)
    return
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias