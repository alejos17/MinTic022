""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Alejandro Tamayo
    Junio 2-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
diccionario={"1":9,"2":8,"3":7,"4":6,"5":0,"6":4,"7":3,"8":2,"9":1,"0":5,":":":","-":"-"}

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
  msg_lista=msg.split()
  print("mensaje en lista: ",msg_lista)

  num=[]  #se crea lista para guardar solamente los numeros y simbolo : y -
  for element in msg:  #Comenzar en 0 e ir hasta la cantidad de la cadena
      if element.isdigit() or element==":" or element=="-":
        num.append(element)  #Si lo encuentra en la cadena lo agrega
        

  print("Numeros: ",num)

  #TODO pasarlos por el diccionario para codificarlos

  numc=[]   #lista para guardar los numeros codificados
  for element in num:   #recorre la lista de numeros
    if element in diccionario:   #compara cada elemento con el diccionario
      numc.append(diccionario[element]) #guarda el resultado del diccionario

  #TODO re-armar la cadena como estaba con los nuevos numeros
  horanumc=[]  #Guarda la hora modificada
  telnumc=[]   #Guarda el telefono modificado
  for i in range(0,5):   #Recorrer la hora
    horanumc.append(numc[i])  #Agrega los numeros de la hora que son los primeros 5
  #El contador i continua sobre la lista de numeros modificados
  for i in range(i,len(numc)):
    telnumc.append(numc[i])  #Agrega los numeros del telefono que son el resto
  
  strtelnumc= "".join(str(_) for _ in telnumc)  
  strhoranumc= "".join(str(_) for _ in horanumc) #Pasa una lista a String, concatena
  print("Numeros cambiados: ",strhoranumc)

  print("El mensaje codificado es: ",msg_lista[0],strhoranumc,msg_lista[2],strtelnumc)

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