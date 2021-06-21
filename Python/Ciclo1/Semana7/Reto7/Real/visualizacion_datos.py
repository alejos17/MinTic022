""" Reto 7 Informes de Vacunacion #
    Alejandro Tamayo
    Junio 21-2021 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt

#IV_07_RS_02
def leer_archivo():
    """ 
    Parameters
    ----------
    Returns
    -------
    datos: Dataframe con los datos 
    """
    datos = pd.read_csv("/home/alejos17/Documentos/code_alejos17/MinTic022/Python/Ciclo1/Semana7/Reto7/Real/col.csv")
    #Mensaje al usuario
    print("*************************************************************")
    print("Archivo .csv cargado")
    print("*************************************************************")
    return datos

#IV_07_RS_03
def graficos_menu(datos):
    """ 
    Parameters
    ----------
    datos: Dataframe con datos del Covid
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
        print("3. Nuevos Casos Diarios")
        print("4. Pruebas Covid-19")
        print("5. Volver Atrás")
        print("---------------------------------------")
        a=int(input("Escriba la opcion: "))
        #Según lo seleccionado por el usuario, se prepara la información para la gráfica
        if a==1:
            Y = datos.iloc[0:,4].values # Total de Casos por día
            Z = datos.iloc[0:,7].values # Total de Muertes por día
            W = ""
            X = datos.iloc[0:,3] # fecha    
            titulo = "Histórico de Contagios COVID-19 en Colombia"
            ly = "Contagios"
            lz = "Muertes"
            ly2 = "Millones de Personas"
            lx = "Entre Marzo 2020 y Junio 2021"
            lw = ""
            ig = 1
            graficar(X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig)
        elif a==2:
            Y = datos.iloc[0:,35].values # Primeras Dosis Aplicadas
            Z = datos.iloc[0:,36].values # Segundas Dosis Aplicadas
            W = datos.iloc[0:,34].values # Total de Vacunas
            X = datos.iloc[0:,3] # fecha
            titulo = "Avance de Vacunación COVID-19 en Colombia"
            ly = "Primera Dosis Aplicadas"
            lz = "Segunda Dosis Aplicadas"
            ly2 = "Cantidad Vacunas en Millones"
            lx = "Inicio Jornada Vacunación en Colombia 17-Feb-2021"
            lw = "Total de Vacunas Adquiridas"
            ig = 2
            graficar(X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig)
        elif a==3:
            Y = datos.iloc[0:,5].values # Nuevos Casos por Día
            Z = datos.iloc[0:,8].values # Nuevas Muertes Por Día
            W = ""
            X = datos.iloc[0:,3] # fecha
            titulo = "Casos vs Muertes Diarias"
            ly = "Casos"
            lz = "Muertes"
            ly2 = "Cantidad de Personas"
            lx = "Entre Marzo 2020 y Junio 2021"
            lw = ""
            ig = 3
            graficar(X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig)        
        elif a==4:
            Y = datos.iloc[0:,28].values # Nuevas pruebas por mil habitantes
            Z = ""
            W = datos.iloc[0:,31].values # Rate Positivo de pruebas por día
            X = datos.iloc[0:,3] # fecha
            titulo = "Pruebas Covid-19 en Colombia"
            ly = "Pruebas Realizadas por cada 1000 hab."
            lz = ""
            ly2 = "Cantidad de Pruebas"
            lx = ""
            lw = "Ratio de Positivos por día"
            ig = 4
            graficar(X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig)
        elif a==5: break
        else: print("Opción no válida, intente de nuevo")
                
    return None

#IV_07_RS_04
def graficar(X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig):
    """ 
    Parameters
    ----------
    X,Y,Z,W,titulo,ly,ly2,lz,lx,lw,ig: String
        Variables con cada uno de los datos de los ejes, y titulos para la gráfica
    Returns
    -------
        Imprime en Pantalla la gráfica solicitada
    """
    plt.style.use('seaborn') #Estilo de la gráfica
    plt.figure()  #Nueva figura
    ax = plt.axes()  #Variable para los componentes de la figura
    ax.set_xlabel(lx,size=14)  #Tamaño de fuente para labels de los ejes
    ax.set_ylabel(ly2,size=14)

    plt.xticks(color='#FFFFFF') #Label eje X en blanco ya que son muchos y no se ven bien
    plt.yticks(size=8)   # Tamaño del eje Y
    plt.title(titulo,size=30) #Titulo de la gráfica
    
    #Bandera para saber que vectores graficar segun el grafico
    if ig==1:
        ax.plot(X,Y,color='#0f5396',linewidth=2,label=ly)
        ax.plot(X,Z,color='#960f0f',linewidth=2,label=lz)
    elif ig==2:
        ax.plot(X,W,color='#095e13',linewidth=2,label=lw)
        ax.plot(X,Y,color='#3a62bd',linewidth=2,label=ly)
        ax.plot(X,Z,color='#663abd',linewidth=2,label=lz)
    elif ig==3:
        plt.bar(X,Y,label=ly,color='#8c9190')
        plt.bar(X,Z,label=lz,color='#bd0202')
    elif ig==4:
        plt.bar(X,Y,label=ly,color='#4da4d6')
        plt.bar(X,W,label=lw,color='#d64d4d')
    
    plt.legend()
    plt.show()
    return None

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias