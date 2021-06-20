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
        print("1. Departamento")
        print("2. Contagios")
        print("3. Muertes")
        print("4. Genero")
        #print("5. ")
        #print("6. Grafico por Fecha de Vacunación")
        #print("7. Grafico por Hora de Vacunación")
        print("8. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        #Según lo seleccionado por el usuario, se carga en la variable b el dato que se requiere graficar
        if a==1: b="nombre_departamento"
        elif a==2: b="fecha_de_inicio_de_sintomas"
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
        a=getattr(datos, b).value_counts()
        a=a.reset_index(name='A')
        a["index"]=pd.to_datetime(a["index"])
        a=a.sort_values(["index"])

        print(a)
        print(type(a))
        grafico_tendencia(a)
        #Si la opción selecciona es por "Etapa", se agrega a los nombres para graficar la palabra
        #"Etapa", ya que en la tabla el valor es 1 o 2 o 3 etc.  Esto es solamente estetico al 
        #momento de gráficar.
        #if a==3:
        #    for x in range(len(nombres)):
        #        nombres[x]=b+" "+str(nombres[x])
        
        #Se envian los datos devueltos por "calculo_datos" a la función graficador para desplegar
        #la imagen en pantalla.
        #graficador(a)
    return None

def grafico_tendencia(a):
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

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias