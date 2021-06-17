""" Taller 2.2 Espacios de Color #
    Alejandro Tamayo
    Mayo 13-2021"""

# Definición de Funciones (Dividir)

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
def convertir_yiq_a_rva(y,i,q):
  """ 
  Parameters
  ----------
  y,i,q:float
     valores del espacio de color YIQ
  Returns
  -------
  r,v,a:float
     valores del espacio de color RVA    
  """ 
  r = y+0.955*i+0.618*q
  v = y-0.271*i-0.645*q
  a = y-1.11*i+1.7*q

  return r,v,a
#-------------------------------------------
def convertir_yiq_a_ycbcr(y,i,q): 
  """ 
  Parameters
  ----------
  y,i,q:float
     valores del espacio de color YIQ
  Returns
  -------
  Y,cb,cr:float
     valores del espacio de color YCbCr
  """ 
  #Se hace aqui la conversión intermedia
  r = y+0.955*i+0.618*q
  v = y-0.271*i-0.645*q
  a = y-1.11*i+1.7*q 
  
  #Se hace aqui la conversión que se pide
  Y = 0.299*r+0.587*v+0.114*a
  cb = 0.1687*r-0.3313*v-0.5*a
  cr = 0.5*r-0.418*v+0.0813*a

  return Y,cb,cr
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def convertir_rva_a_yiq(r,v,a):
  """ 
  Parameters
  ----------
  r,v,a:float
     valores del espacio de color rva
  Returns
  -------
  y,i,q:float
     valores del espacio de color yiq
  """ 
  #Se realiza conversion directa
  y=0.299*r+0.587*v+0.114*a
  i=0.596*r-0.275*v-0.321*a
  q=0.212*r-0.528*v+0.311*a
  #Retorno de valor yiq
  return y,i,q
#-------------------------------------------
def convertir_rva_a_ycbcr(r,v,a):
  """ 
  Parameters
  ----------
  r,v,a:float
     valores del espacio de color rva
  Returns
  -------
  Y,cb,cr:float
     valores del espacio de color YCbCr
  """ 
  #Se realiza conversion directa
  y=0.299*r+0.587*v+0.114*a
  cb=0.1687*r-0.3313*v-0.5*a
  cr=0.5*r-0.418*v+0.0813*a
  #Retorno de valor ycbcr
  return y,cb,cr
#-------------------------------------------
def convertir_ycbcr_a_rva(y,cb,cr):
  """ 
  Parameters
  ----------
  Y,cb,cr:float
     valores del espacio de color YCbCr
  Returns
  -------
  r,v,a:float
     valores del espacio de color rva
  """ 
  #Se realiza conversión directa
  r=y+1.402*cr
  v=y+0.344*cb-0.714*cr
  a=y+1.772*cb
  return r,v,a 

def convertir_ycbcr_a_yiq(y,cb,cr):
  """ 
  Parameters
  ----------
  Y,cb,cr:float
     valores del espacio de color YCbCr
  Returns
  -------
  y,i,q:float
     valores del espacio de color yiq
  """ 
  #Se debe calcular primero de ycbcr a rva llamando la funcion anterior para no
  #repetir texto
  #Se guardan los valores rva en variables temporales
  r1,v1,a1=convertir_ycbcr_a_rva(y,cb,cr)
  
  #Con los datos temporales de rva se calcula yiq
  y=0.299*r1+0.587*v1+0.114*a1
  i=0.596*r1-0.275*v1-0.321*a1
  q=0.212*r1-0.528*v1+0.311*a1
  return y,i,q 


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Inicio de la bandera en 1 para que entre en el bucle while
op=1

#Bucle que inicia el menú del programa
#Si la bandera se encuentra entre 1 y 7 es opción valida y entra al bucle.
while 1<=op<=7:
#Se muestra menú del programa
  print(" ")
  print(" ")
  print("Hola, bienvenido al conversor de color")
  print("Por favor ingrese la opcion que necesita")
  print("1. YIQ a rva")
  print("2. YIQ a YCbCr")
  print("3. rva a YIQ")
  print("4. rva a YCbCr")
  print("5. YCbCr a rva")
  print("6. YCbCr a YIQ")
  print("7. Salir")
  print(" ")
#variable op guarda la opción seleccionada por el usuario
  op=int(input("Escriba el numero de la conversión a realizar:  "))
#Condicional donde se trabaja solamente la opción indicada por el usuario
  if op==1:  #de YIQ a rva
    print(" ")
    print("Bienvenido, vamos a convertir de YIQ a rva")
    y = float(input("Digite el valor de Y:"))
    i = float(input("Digite el valor de I:"))
    q = float(input("Digite el valor de Q:"))
    rt,vt,at= convertir_yiq_a_rva(y,i,q) #Se llama función y se guarda resultado
    print("la conversión de yiq a rva es","r=",rt,"v=",vt,"a=",at)
  elif op==2: #de YIQ a YCbCr
    print(" ")
    print("Bienvenido, vamos a convertir de YIQ a YCbCr")
    y = float(input("Digite el valor de Y:"))
    i = float(input("Digite el valor de I:"))
    q = float(input("Digite el valor de Q:"))
    yt,cbt,crt=convertir_yiq_a_ycbcr(y,i,q)
    print("la conversión de yiq a ycbcr es","y=",yt,"cb=",cbt,"cr=",crt)
  elif op==3:
    print(" ")
    print("Bienvenido, vamos a convertir de rva a YIQ")
    r = float(input("Digite el valor de r:"))
    v = float(input("Digite el valor de v:"))
    a = float(input("Digite el valor de a:"))
    yt,it,qt=convertir_rva_a_yiq(r,v,a)
    print("la conversión de rva a YIQ es","Y=",yt,"I=",it,"Q=",qt)
  elif op==4:
    print(" ")
    print("Bienvenido, vamos a convertir de rva a YCbCr")
    r = float(input("Digite el valor de r:"))
    v = float(input("Digite el valor de v:"))
    a = float(input("Digite el valor de a:"))
    yt,cbt,crt=convertir_rva_a_ycbcr(r,v,a)
    print("la conversión de rva a YCbCr es","Y=",yt,"Cb=",cbt,"Cr=",crt)
  elif op==5:
    print(" ")
    print("Bienvenido, vamos a convertir de YCbCr a rva")
    y = float(input("Digite el valor de Y:"))
    cb = float(input("Digite el valor de Cb:"))
    cr = float(input("Digite el valor de Cr:"))
    rt,vt,at=convertir_ycbcr_a_rva(y,cb,cr)
    print("la conversión de YCbCr a rva es","r=",rt,"v=",vt,"a=",at)
  elif op==6:
    print(" ")
    print("Bienvenido, vamos a convertir de YCbCr a YIQ")
    y = float(input("Digite el valor de Y:"))
    cb = float(input("Digite el valor de Cb:"))
    cr = float(input("Digite el valor de Cr:"))
    yt,it,qt=convertir_ycbcr_a_yiq(y,cb,cr)
    print("la conversión de rva a YIQ es","Y=",yt,"I=",it,"Q=",qt)
  elif op==7: #Opción para salir del programa despliega mensaje y sale del bucle
    print("FIN DE PROGRAMA")
    break #salida del bucle y por tanto del programa
  else:  #Esta opcion es cuando el usuario marca otro numero diferente a las opciones.
    op=1. #Se reinicia la bandera en 1 para que pueda volver a entrar al menu
    print("Error en la opción del programa por favor indique de nuevo")
 
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================