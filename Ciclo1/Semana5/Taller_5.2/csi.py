""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Alejandro Tamayo
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
diccionario={"1":9,"2":8,"3":7,"4":6,"5":0,"6":4,"7":3,"8":2,"9":1,"0":5}

print(diccionario)
#print(diccionario[3])

def codificar_mensaje(msg):
  """ 
  Parameters
  ----------
  mensaje_original:string
    Una cadena con el mensaje a codificar 
  Returns
  -------
  mensaje_codificado:string
    El mensaje codificado con la estrategia saltando al 5    
  """
  #TODO desglosar la cadena para sacar los digitos
  num=[]
  for element in msg:  #Comenzar en 0 e ir hasta la cantidad de la cadena
      if element.isdigit():
        num.append(element)

  print("Numeros: ",num)

  #TODO pasarlos por el diccionario para codificarlos

  msgc=[]
  for element in num:
    if element in diccionario:
      msgc.append(diccionario[element])

  #TODO re-armar la cadena como estaba con los nuevos numeros
  

  
  print("Numeros cambiados: ",msgc)

  return "No implementado"

def decodificar_mensaje(mensaje_codificado):
  """ 
   Parameters
   ----------
   mensaje_codificado:string
     Una cadena con el mensaje codificado
   Returns
    -------
   mensaje_codificado:string
     El mensaje original decodificado
  """  

  return "No implementado"