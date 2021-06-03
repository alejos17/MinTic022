""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Alejandro Tamayo
    Junio 3-2021 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
#Diccionario creado con cada uno de los movimientos segun el codigo saltanto al 5
diccionario={"1":9,"2":8,"3":7,"4":6,"5":0,"6":4,"7":3,"8":2,"9":1,"0":5,":":":","-":"-"}

def codificar_mensaje(msg):
  """ 
  Parameters
  ----------
  msg:string
    Una cadena con el mensaje a codificar 
  Returns
  -------
    imprime en pantalla al usuario  
  """
  #desglosar la cadena para sacar los digitos
  print("El mensaje a codificar es: ",msg)
  print("\n")

  msg_lista=msg.split()
  
  num=[]  #se crea lista para guardar solamente los numeros y simbolo : y -
  for element in msg:  #Comenzar en 0 e ir hasta la cantidad de la cadena
      if element.isdigit() or element==":" or element=="-":
        num.append(element)  #Si lo encuentra en la cadena lo agrega
      
  #pasarlos por el diccionario para codificarlos
  numc=[]   #lista para guardar los numeros codificados
  for element in num:   #recorre la lista de numeros
    if element in diccionario:   #compara cada elemento con el diccionario
      numc.append(diccionario[element]) #guarda el resultado del diccionario

  #re-armar la cadena como estaba con los nuevos numeros
  horanumc=[]  #Guarda la hora modificada
  telnumc=[]   #Guarda el telefono modificado
  for i in range(0,5):   #Recorrer la hora
    horanumc.append(numc[i]) #Agrega los numeros de la hora que son los primeros 5
    i+=1  
  #El contador i continua sobre la lista de numeros modificados
  for i in range(i,len(numc)):
    telnumc.append(numc[i])  #Agrega los numeros del telefono que son el resto
  
  #Funcion .join para concatenar listas a string
  strtelnumc= "".join(str(_) for _ in telnumc)  
  strhoranumc= "".join(str(_) for _ in horanumc) #Pasa una lista a String, concatena
  
  #Se arma la cadena nuevamente con la posicion de cada palabra del mensaje en la misma
  #posicion y se agregan los numeros modificados.
  print("El mensaje codificado es: ",msg_lista[0],msg_lista[1],msg_lista[2],msg_lista[3],strhoranumc,msg_lista[5],msg_lista[6],strtelnumc)

  return

"""
def decodificar_mensaje(mensaje_codificado):

   Parameters
   ----------
   mensaje_codificado:string
     Una cadena con el mensaje codificado
   Returns
    -------
   mensaje_codificado:string
     El mensaje original decodificado


  return "No implementado"
"""