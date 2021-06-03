""" Modulo para el manejo de datos de dispositivos IoT 
    Alejandro Tamayo
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
from collections import namedtuple
#----------Definición de Funciones (Dividir)------------
#tipo_dispositivo1,identificador1,estado1@tipo_dispositivo2,identificador2,estado2

def separar_cadenas(comando):
    """ 
    Parameters
    ----------
    comando:string
        Una cadena con los datos de todos los IoT de una smarth-home 
    Returns
    -------
    lista_IoT:[(namedtuple)]
        una lista de tuplas cada una de ellas con los datos de un dispositivo IoT     
    """
    #Realizamos un split por tipo de dispositivo.
    iot=namedtuple('IoT',['dispositivo','id','valor']) #Tupla con los datos 
    x = comando.split("@")   #Lista creada con cada item
    print(x)
    i=0
    for i in range(len(x)):
      print(" ")
      y=x[i]
      z=y.split(",")
      print("Desplegado por coma: ",z)
      a=z[0]
      b=z[1]
      c=z[2]
      print("A: ",a," B:",b," C:",c)
      d=iot(a,b,c)
      print("Tupla llena: ",d)
      

    print(" ")
    print(iot)
    #TODO crear una lista para ir guardando las tuplas con los
    #valores, luego recorrer la lista la posicion i de la lista
    #y cargando lo que necesite ej.  x[i].dispositivo  o id
    
    #TODO
    #Crear un for que recorra x y saque en 3 variables cada dato,
    #luego crear una tupla con nombre y guardar esos datos en la
    #estructura creada, luego de tener la tupla, se puede pedir valores
    #por tipo de dispositivo o tipo de dato etc.  



    return "No implementado"


def calcular_estadisticas(lista_IoT):
  """ 
  Parameters
  ----------
 lista_IoT:[(namedtuple)]
    Una lista de tuplas con los datos de los dispositivos IoT 
  Returns
  -------
  estadistica:(total_on, total_off)
    una tupla con  el total de dispositivos IoT en estado ON y otra con el total de estado     
  """  
  return "No implementado"