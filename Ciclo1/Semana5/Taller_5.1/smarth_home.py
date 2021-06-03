""" Modulo para el manejo de datos de dispositivos IoT 
    Alejandro Tamayo
    Junio 3-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
from collections import namedtuple
#----------Definición de Funciones (Dividir)------------
def separar_cadenas(comando):
    """ 
    Parameters
    ----------
    comando:string
        Una cadena con los datos de todos los IoT de una smarth-home 
    Returns
    -------
    registros:[(namedtuple)]
        una lista de tuplas cada una de ellas con los datos de un dispositivo IoT     
    """
    #Realizamos un split por tipo de dispositivo.
    registros=[]  #Creación de lista para guardar las tuplas
    iot=namedtuple('IoT',['dispositivo','id','valor']) #Tupla con los datos 
    x = comando.split("@")   #Lista creada con cada dispositivo
        
    for i in range(len(x)):  #Recorrer la lista para sacar cada dato
      y=x[i]                 #Copia de la lista
      z=y.split(",")         #Separar por comas
      a=z[0]                 #Guardar primer dato
      b=z[1]                 #Guardar segundo dato
      c=z[2]                 #Guardar tercer dato
      d=iot(a,b,c)           #Crear tupla IoT con cada valor
      registros.append(d)    #Agregar la tupla a la lista

    return registros


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
  #TODO reporte cantidad de dispositivos que estan en ON y en OFF
  repon=[]   #Lista para dispositivos en ON
  repoff=[]  #Lista para dispositivos en OFF
  for i in range(len(lista_IoT)):    #Recorrer tupla
    if lista_IoT[i].valor=="ON":     #Para valores en ON
      repon.append(lista_IoT[i].dispositivo)      #Agregar a la lista
      repon.append(lista_IoT[i].id)
      repon.append(lista_IoT[i].valor)
    elif lista_IoT[i].valor=="OFF":   #Para valores en OFF
      repoff.append(lista_IoT[i].dispositivo)   #Agregar a la lista
      repoff.append(lista_IoT[i].id)
      repoff.append(lista_IoT[i].valor)

  print("\n")
  print("=======================================================================")
  print("*** Dispositivos Activados ***")
  for i in range(len(repon)):
    print(repon[i])
    

  print("\n")
  print("=======================================================================")
  print("*** Dispositivos Desactivados ***")
  for i in range(len(repoff)):
    print(repoff[i])
    
    

  return