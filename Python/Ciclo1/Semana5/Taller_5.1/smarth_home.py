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
    Imprime en pantalla el resultado de la estadistica, dispositivos en ON y en OFF     
  """
  liston=[]   #Lista para dispositivos en ON
  listoff=[]  #Lista para dispositivos en OFF
  repon=namedtuple('ON',['dispositivo','id','valor'])   #Tupla para dispositivos en ON
  repoff=namedtuple('OFF',['dispositivo','id','valor'])  #Tupla para dispositivos en OFF
  for i in range(len(lista_IoT)):    #Recorrer tupla
    if lista_IoT[i].valor=="ON":     #Para valores en ON
      #Se crea una tupla por dispositivo
      on=repon(lista_IoT[i].dispositivo,lista_IoT[i].id,lista_IoT[i].valor)
      liston.append(on)   #Se agrega a la lista de dispositivos ON
    elif lista_IoT[i].valor=="OFF":   #Para valores en OFF
      #Se crea una tupla por dispositivo
      off=repoff(lista_IoT[i].dispositivo,lista_IoT[i].id,lista_IoT[i].valor)
      listoff.append(off)   #Se agreda a la lista de dispositivos OFF

  #Mensajes en pantalla para el usuario con las estadisticas
  #Imprimiendo las listas generadas de ON y OFF
  print("\n")
  print("=======================================================================")
  print("*** Dispositivos Activados ***")
  print("Total: ",len(liston))
  for i in range(len(liston)):
    print(liston[i])
    

  print("\n")
  print("=======================================================================")
  print("*** Dispositivos Desactivados ***")
  print("Total: ",len(listoff))
  for i in range(len(listoff)):
    print(listoff[i])
  
  return