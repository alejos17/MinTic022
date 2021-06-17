""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Alejandro Tamayo
    Mayo 19-2021 """

#---------------- Zona librerias------------
import multas as m

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def bienvenida():
    """ 
  Parameters
  ----------
  Se realiza impresión en pantalla de mensaje de bienvenida
  """
    print("Bienvenido al Taller 3, Semana 3 de MicTIC2022")
    print("esta pequeña aplicación intenta resolver el siguiente problema")
    print(" ")
    print("El Radar")
    print(" ")
    print("Dadas las dos distancias obtenidas del vehículo y el lapso de tiempo, calcular si debe pagar una multa o no")
    print(" ")
    print(" ")
    print("Con los datos que vamos a solicitar a continuación evaluaremos la solución propuesta")
    print(" ")
    print(" ")

def solicitud_datos():
  """ 
  Parameters
  ----------
  Returns
  -------
  a,b,t:float
       devuelve los valor tomados por teclado
  """ 
  print(" ")
  a=float(input("Por favor indique la distancia inicial marcada por el radar (metros): "))
  b=float(input("Por favor indique la distancia final marcada por el radar (metros): "))
  t=float(input("Por favor indique el tiempo transcurrido marcado por el radar (segundos): "))
  return a,b,t

def calculo_velocidad(pa,pb,tt):
  """ 
  Parameters
  ----------
  pa,pb,tt:float
    punto a, punto b y tiempo tomados del radar
  Returns
  -------
  v:float
    Calcula la velocidad y devuelve el valor
  """ 
  r=pa-pb  #Calcula el recorrido R
  r=r/1000 #Convierte R de metros a Kilometros
  t=tt/3600  #Convierte el tiempo de segundos a horas
  v=r/t   #Formula de velocidad = distancia / tiempo
  v=round(v,1)  #Redondeo de velocidad con solo 1 decimal
  
  return v

def hacer_alcoholemia():
    """ 
  Parameters
  ----------
  Returns
  -------
  tipomulta:float
  mensaje:string
     Devuelte el tipo de multa y el mensaje con el detalle de la multa por alcoholemia
  """ 
    print("")
    print("")
    print("Este tipo de multa requiere de la medicion adicional de alcholemia")
    print("Se debe realizar medicion con detector e ingresar los valores")
    print("Datos requeridos: Nivel de miligramos de etanol / 100 ml de sangre")
    print("")
    ga=float(input("Por favor indique el valor marcado por el detector:  "))
    print("")
    print("Debido a que el nivel de alcohol en sangre es de: ",ga," mg de etanol / 100 ml de sangre, se decreta: ")
    tipomulta,mensaje=m.multar_alcoholemia(ga)
    return tipomulta,mensaje

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
bienvenida()  #Inicio del programa, mensajes de inicio
pa,pb,tt=solicitud_datos() #Solicitamos al usuario datos requeridos
vel=calculo_velocidad(pa,pb,tt) #Calculo de la velocidad
tipomulta,mensaje=m.multar_velocidad(vel) #Con la velocidad, miramos las multas a aplicar
print("")
print("")
print("La velocidad calculada es de: ",vel," Km/h") #Imprimir por pantalla la velocidad
print("")
print("Según la velocidad esta catalogado como tipo: ",tipomulta) #Indica el tipo de multa
print("Detalles: ",mensaje) #Muestra mensaje al usuario de la multa según la velocidad

#Si la velocidad supera los 81 Km/h
#En este caso es lo mismo que el tipo de multa 4 y 5 de la funcion de velocidad
if tipomulta==4 or tipomulta==5:
  ma,men=hacer_alcoholemia()  #Se llama funcion para verificar alcoholemia
  print("")
  print("")
  print(men)  #Se imprime mensaje necesario segun el dato de alcholemia en la funcion (ga)
