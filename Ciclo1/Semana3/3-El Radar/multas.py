""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Alejandro Tamayo
    Mayo 19-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(vel):
  """ 
  Parameters
  ----------
  v:float
    Indica la velocidad a la que iba el vehiculo
  Returns
  -------
  m:float
  msg:string
     Indica el tipo de multa y el mensaje a desplegar con el detalle de la multa
  """ 
  if 1<vel<20:
    m=1
    msg="llamado de atención por baja velocidad"
  elif 21<vel<60:
    m=2
    msg="Normal"
  elif 61<vel<80:
    m=3
    msg="llamdo de atención por alta velocidad"
  elif 81<vel<120:
    m=4
    msg="Multa por exceso de velocidad Tipo I"
  elif vel>120:
    m=5
    msg="Multa por exceso de velocidad Tipo II e inmovilización del vechículo"
  
  return m,msg


def multar_alcoholemia(ga):
  """ 
  Parameters
  ----------
  ga:float
    Indica lso grados de alcohol encontrados en la prueba
  Returns
  -------
  m:float
  msg:string
     Indica el tipo de multa y el mensaje a desplegar con el detalle de la multa
  """ 
  if 20<ga<39:
    m=1
    msg="además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
  elif 40<ga<99:
    m=2
    msg="adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
  elif 100<ga<149:
    m=3
    msg="adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
  elif ga>150:
    m=4
    msg="adicionalmente a la sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
  
  return m,msg