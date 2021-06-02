""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Alejandro Tamayo
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
diccionario={1:9,2:8,3:7,4:6,5:0,6:4,7:3,8:2,9:1,0:5}

print(diccionario)
print(diccionario[3])

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
  msgc=[]
  msg=eval(msg)

  for element in msg:
    if element in diccionario:
      msgc.append(diccionario[element])

  print(msgc)

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