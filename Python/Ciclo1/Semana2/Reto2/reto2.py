""" Reto 2 Protegiendo al castillo medieval  #
    Alejandro Tamayo
    Mayo 15-2021 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def bienvenida():
  """ 
  Parameters
  ----------
  Se realiza impresión en pantalla de mensaje de bienvenida
  """ 
  print(" ")
  print("Bienvenido al Reto Semana 2 de MicTIC2022")
  print("esta pequeña aplicación intenta resolver el siguiente problema")
  print(" ")
  print("La puerta del castillo")
  print(" ")
  print("El rey Arturito (antecesor de R2D2), está muy preocupado porque le han informado que el ejército Vaderiano está muy cerca de su castillo con la idea de atacarlo. El castillo se encuentra realmente muy bien protegido por murallas y cañones, pero su talón de Aquiles es la gran puerta del castillo, que solo se puede cerrar bajo ataque, porque por allí entran víveres, productos y medicinas. El problema es que se demoran mucho para cerrarla ya que esto se hace empujándola de abajo hacia arriba por los soldados Chewbaccas, que a pesar de su fuerza, en ocasiones no alcanzan a cerrarla completamente y el castillo es saqueado. A oídos del rey ha llegado un plano elaborado por un tal Arquímedes (se sospecha que es un seudónimo) donde le plantea una solución al problema aunque no da muchos detalles. Aquí reproducimos el dibujo y las instrucciones.")
  print(" ")
  print(" ")
  print("Con los datos que vamos a solicitar a continuación evaluaremos la solución propuesta y estas preguntas: ")
  print(" ")
  print("1. Cuantas vueltas se debe dar a la polea para cerrar la puerta? ")
  print("2. Cuantos Chewbaccas son necesarios? (Cada uno puedar solo 3 vueltas) ")
  print("3. A un tiempo dado para que se cierre la puerta, a que velocidad se debe girar la polea? ")
  print(" ")
  print(" ")


def solicitud_datos():
  """"
  Parameters
  ----------
  Returns
  -------
  p,po,tt:float
     Valores recogidos por teclado que indica el usuario
  """ 
  p=float(input("Por favor indique la longitud de la puerta en metros: "))
  print(" ")
  po=float(input("Por favor indique el perimetro de la polea en centimetros: (50 cms)  "))
  print(" ")
  t=float(input("En cuanto tiempo desea que se cierre la puerta? (En minutos):  "))
  print(" ")
  return p,po,t

def calculos(pt,pot,tt):
  """"
  Parameters
  ----------
  pt,pot,tt:float
     Valores de longitud de puerta, polea y tiempo
  Returns
  -------
  c,cm,v,ch,ts,vel:float
     Valores de tamaño de la cuerda, vueltas, cantidad de chewbaccas, tiempo y velocidad
  """ 
  #Se realiza import de la libreria math para calulo de teorema de pitágoras  
  import math 
  m=pt  #Se asigna mismo valor de la puerta al muro
  c=math.sqrt((m**2)+(pt**2)) #Calculo de pitagoras
  c=round(c,2) #Se redonda el valor de c a solo 2 decimales
  cm=c*100  #Se convierte de metros a centimetros
  radio=pot/2 #Se calcula el radio de la polea: diametro / 2
  per=2*radio*math.pi  #Se calcula el perimetro de la polea 
  per=round(per,0) #Se redondea valor sin decimales
  v=cm/per  #Se calculan las vueltas sobre el diametro de la polea
  v=round(v,0) #Se redondea el valor sin decimales
  ch=v/3  #Se divide en tres vueltas que hace cada Chewbacca y nos da la cantidad
  ch=round(ch,0) #Se redondea el valor sin decimales 
  ts=tt*60  #Se convierten minutos en segundos
  vel=cm/ts #Se divide el tiempo en la distancia para calcular la velocidad
  vel=round(vel,2) #Se redondea el valor con 2 decimales
  return c,cm,v,ch,ts,vel  #Se retornan todos los valores calculados

def mensajes(pt,pot,tt,ct,cmt,vt,cht,tst,velt):
  print(" ")
  print("=============================================================================== ")
  print("Longitud de puerta: ",pt," metros")
  print("Perimetro de la polea: ",pot," centimetros")
  print("Longitud de Muro: ",pt," metros")
  print("Longitgud de la Cuerda: ",ct," metros o ",cmt," centimetros")
  print("Cantidad de Vueltas para cerrar la puerta: ",vt," vueltas")
  print("Cantidad de Chewbaccas necesarios para cerrar la puerta: ",cht," chewbaccas")
  print("Tiempo requerido para cerrar la puerta: ",tt," minutos o ",tst," segundos")
  print("Velocidad necesaria para cerrar en ese tiempo: ",velt," cm/seg")
  print("=============================================================================== ")
#Secuencia general del programa

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
op=1  #Bandera inicial para arrancar el bucle

while op==1:  #Bucle para dar la opcion al programa de continuar con otros valores
  bienvenida()  #Invocación de funcion de bienvenida con mensajes iniciales
  pt,pot,tt=solicitud_datos() #Invocación de funcion para toma de datos necesarios
  ct,cmt,vt,cht,tst,velt=calculos(pt,pot,tt) #Invocación para el calculo necesario
  mensajes(pt,pot,tt,ct,cmt,vt,cht,tst,velt) #Invocación para desplegar los resultados
  #Mensaje y condicional para solicitar al usuario si quiere continuar con otros valores
  op=float(input("Desea continuar con el programa ingresando nuevos datos? 1. Si    "))
  if op==1:   #Si el usuario selecciona 1 el bucle continua y vuelve a comenzar el programa
    print("======================== ")
    print("Reiniciando programa")    # Indica mensaje de que va arrancar de nuevo
    print("======================== ")
  else:    # Si el usuario selecciona otra opcion entonces el programa se termina
    print("======================== ")
    print("FIN DEL PROGRAMA, MUCHAS GRACIAS!")    # Indica mensaje de terminación.
    print("======================== ")
    break
  

#======================================================================
#  Documentación del programa y resolución con el metodo IDEAL en el archivo
#  Reto 2.docx
# =====================================================================