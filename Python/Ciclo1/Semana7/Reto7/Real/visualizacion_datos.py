""" Reto 7 Informes de Vacunacion #
    Tu nombre aquí
    Junio XX-XX """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
#Traer datos reales para graficas de covid-19 en Colombia
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from  sodapy import Socrata

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
    datos = pd.read_csv("/home/alejos17/Documentos/code_alejos17/MinTic022/Python/Ciclo1/Semana7/Reto7/Real/col.csv")
    #Mensaje al usuario
    print("*************************************************************")
    print("Archivo .csv cargado")
    print("*************************************************************")
    return datos

def importar_datos():
    #Acceso al servidor con datos publicos
    client = Socrata("www.datos.gov.co", None)
    #Trae las primeras 20.000 filas y crea un diccionario
    tabla = client.get("gt2j-8ykr", limit=2000)
    #Pasar los datos a un Dataframe
    datos = pd.DataFrame.from_records(tabla)
    return datos

#IV_06_RS_03
def graficos_menu(datos):
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
        print("++++++++++  Generar Grafico +++++++++++")
        print("=======================================")
        print("1. Historico")
        print("2. Vacunación")
        print("3. Muertes")
        print("4. Genero")
        #print("5. ")
        #print("6. Grafico por Fecha de Vacunación")
        #print("7. Grafico por Hora de Vacunación")
        print("8. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        #Según lo seleccionado por el usuario, se carga en la variable b el dato que se requiere graficar
        if a==1: grafico_historico(datos)
        elif a==2: grafico_vacunas(datos)
        elif a==3: b="etapa"        
        elif a==4: b="genero"
        elif a==8: break
        else: print("Opción no válida, intente de nuevo")
                
    return None

def grafico_historico(a):
    Y = a.iloc[0:,4].values # confirmados diarios
    #R = data.iloc[61:,3].values # recuperados diarios
    D = a.iloc[0:,7].values # difuntos diarios
    X = a.iloc[0:,3] # fecha
    
    plt.figure() 
    ax = plt.axes()
    ax.grid(linewidth=0.2, color='#8f8f8f') # CREAR UNA CUADRICULA A LO LARGO DEL GRAFICO
    ax.set_facecolor("black") # FONDO DEL COLOR DEL GRAFICO
    ax.set_xlabel('\nFecha',size=12,color='#4bb4f2')
    ax.set_ylabel('Casos Confirmados\n',
              size=25,color='#4bb4f2')

    plt.xticks(rotation='vertical',size='20',color='white') # MODIFICAR LAS FECHAS Y LA FUENTE DIARIA
    plt.yticks(size=20,color='white')
    plt.tick_params(size=20,color='white')
  
    #for i,j in zip(X,Y):
    #    ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
    
    plt.title("Historico COVID-19 en Colombia\n",
          size=30,color='#28a9ff')
  
    ax.plot(X,Y,color='#1F77B4',linewidth=1,label='Contagios')
    ax.plot(X,D,color='#b4331f',linewidth=1,label='Muertes')
    plt.legend()

    plt.show()
    return None

def grafico_vacunas(a):
    Y = a.iloc[0:,35].values # Personas Vacunadas
    R = a.iloc[0:,36].values # Segundas Dosis
    D = a.iloc[0:,34].values # Total de Vacunas
    X = a.iloc[0:,3] # fecha
    
    plt.figure() 
    ax = plt.axes()
    ax.grid(linewidth=0.2, color='#8f8f8f') # CREAR UNA CUADRICULA A LO LARGO DEL GRAFICO
    ax.set_facecolor("black") # FONDO DEL COLOR DEL GRAFICO
    #ax.set_xlabel('\nFecha',size=12,color='#4bb4f2')
    #ax.set_ylabel('Casos Confirmados\n',
              #size=25,color='#4bb4f2')

    plt.xticks(rotation='vertical',size='20',color='white') # MODIFICAR LAS FECHAS Y LA FUENTE DIARIA
    plt.yticks(size=20,color='white')
    plt.tick_params(size=20,color='white')
  
    #for i,j in zip(X,Y):
    #    ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
    
    plt.title("Vacunación COVID-19 en Colombia\n",
          size=30,color='#28a9ff')
  
    ax.plot(X,Y,color='#dd42f5',linewidth=1,label='Primera Dosis')
    ax.plot(X,D,color='#42f5ec',linewidth=1,label='Total de Vacunas')
    ax.plot(X,R,color='#42f587',linewidth=1,label='Segunda Dosis')
    plt.legend()

    plt.show()
    return None

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias