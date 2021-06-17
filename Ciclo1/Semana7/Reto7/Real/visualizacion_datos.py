""" Reto 7 Informes de Vacunacion #
    Tu nombre aquí
    Junio XX-XX """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
#Traer datos reales para graficas de covid-19 en Colombia
import pandas as pd
import matplotlib.pyplot as plt
from  sodapy import Socrata

def importar_datos():
    #Acceso al servidor con datos publicos
    client = Socrata("www.datos.gov.co", None)

    #Trae las primeras 20.000 filas y crea un diccionario
    tabla = client.get("gt2j-8ykr", limit=2000)

    #Pasar los datos a un Dataframe
    df_tabla = pd.DataFrame.from_records(tabla)

    return df_tabla

#IV_06_RV_07
def graficador(datos):
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
    
    #Agrupar el filtro, en este caso ..  numero de recuperados por departamento
    #conteo_dep_recu = datos.groupby('departamento_nom')['recuperado'].count().plot(kind='barh')
    #conteo_dep_recu.set_xlabel("Personas")
    #conteo_dep_recu.set_title("Deparmentos con numero de Recuperados")

    #Positivos por Sexo por departamentos
    dep_sex_cont = datos.groupby(['departamento_nom','recuperado'])
    z=dep_sex_cont.mean()

    #Conteo simple de una sola columna del dataframe o serie
    #a=datos.departamento_nom.value_counts()
    #b=pd.unique(datos['ciudad_municipio_nom'])
    #plt.barh(a.index, a)

    #print(a)
    #print(type(a))
    print("------------------------------")
    #print(b)
    #print(type(b))
    print("------------------------------")
    print(dep_sex_cont)
    print(type(dep_sex_cont))
    print("------------------------------")
    print(z)
    print(type(z))
    #ax=datos.departamento_nom.value_counts().plot(kind='barh')
    #ax.invert_yaxis()
    #ax.set_xlabel('Cantidad de Personas') #Titulo del eje X
    #ax.set_title('Graficas') # Titulo de la grafica
    
    
    #print(x_values)
    #print("---------------------------")
    #print(y_values)
    """
    #Grafica Vertical para etapa, vacuna y genero, pocos datos
    #Sacado de: https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
    fig, ax = plt.subplots() #Llamando Figura y Ejes
    x_pos = range(len(x_values))  # Valores del eje X, la cantidad de datos encontrados
    ax.bar(x_pos, y_values, align='center') #Barra vertical centradas: cantidad barras, valores, alineación.
    ax.set_xticks(x_pos)  #Asignar valores a las posiciones en eje X
    ax.set_xticklabels("Departamentos") 
    ax.set_ylabel('Cantidad de Personas') #Titulo del eje y
    ax.set_title('Grafica')  #Titulo de la gráfica
    #Grafica Horizontal para mostrar bien cuando son muchos datos
    #sacado de: https://matplotlib.org/stable/gallery/https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-pylines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
    fig, ax = plt.subplots() #Llamando Figura y Eje
    y_pos = range(len(x_values)) #Valores del eje Y, cantidad de datos encontrados
    ax.barh(y_pos, y_values, align='center') #Barra horizontal centradas: cantidad de barras, valores, alineación.
    ax.set_yticks(y_pos) #Asignar valores a las posiciones en eje Y
    ax.set_yticklabels(x_values)
    ax.set_xlabel('Cantidad de Personas') #Titulo del eje X
    ax.set_title('Grafica por '+b) # Titulo de la grafica
    """            
    plt.show()  #Imprimir grafico seleccionado en pantalla
    return None

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================


#Es necesario importar las depencendias necesarias