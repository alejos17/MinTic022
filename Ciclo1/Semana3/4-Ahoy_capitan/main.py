""" Programa para apoyar al marinero Seijo
    Alejandro Tamayo
    Mayo 20-2021 """

import utilidades as util

def bienvenida():
    """ 
  Parameters
  ----------
  Se realiza impresión en pantalla de mensaje de bienvenida
  """
    print("Bienvenido al Taller 4, Semana 3 de MicTIC2022")
    print("esta pequeña aplicación intenta resolver el siguiente problema")
    print(" ")
    print("Ahoy! capitán")
    print(" ")
    print("Indicando la criatura y la ubicación, se debe formar la palabra para alertar al capitán")
    print(" ")
    print(" ")

def solicitar_random():
  """ 
  Parameters
  ----------
  Returns
  -------
  criatura,direccion:String
       Develve la criatura y la ubicación
  """ 
  criatura= util.aparecer_criatura()
  direccion=util.aparecer_direccion()
  return criatura,direccion

def est_criatura(criatura):
  if criatura=="Kraken" or criatura=="Hipocampo" or criatura=="Pulpo":
    msg="un "
    msg += criatura
  elif criatura=="Sirenas" or criatura=="Hidras":
    msg="unas "
    msg += criatura
  elif criatura=="Ballena" or criatura=="Macaraprono":
    msg="una "
    msg += criatura
  elif criatura=="Leviatanes":
    msg="unos "
    msg += criatura
  return msg

def est_ubicacion(ubicacion):
  if ubicacion=="babor" or ubicacion=="estribor":
    msg="a "
    msg += ubicacion
  elif ubicacion=="proa" or ubicacion=="popa":
    msg="por la "
    msg += ubicacion
  return msg    
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento
bienvenida()
criatura,ubicacion=solicitar_random()
print(" ")
print("Criatura dada: ",criatura)
print("Ubicacion dada: ",ubicacion)
print(" ")
mc=est_criatura(criatura)
mu=est_ubicacion(ubicacion)
print("===========================================================")
print("********","Ahoy! capitán,",mc,mu,"********")
print("===========================================================")
print(" ")
print(" ")
print("FIN DE PROGRAMA")