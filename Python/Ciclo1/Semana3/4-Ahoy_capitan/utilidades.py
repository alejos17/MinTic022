""" Modulo generador aleatorio de cadenas #
    Funciones que retornan criaturas marinas
    y ubicaciones del barco 
    Oscar Franco-Bedoya
    Mayo 10-2021 """

import random
# Definición de Funcione
def aparecer_criatura():
  """ 
  Returns
  -------
  criatura:str
  Una de las 8 criaturas de la lista generadas aleatoriamente     
  """
  criaturas=["Kraken","Sirenas","Ballena","Hipocampo","Macaraprono","Pulpo","Leviatanes","Hidras"]
  indice = random.randint(0, 7)
  return criaturas[indice]

def aparecer_direccion():
  """ 
  Returns
  -------
  criatura:str
  Una de las 4 direcciones de la lista generadas aleatoriamente     
  """
  direccion=["babor","estribor","proa","popa"]
  indice = random.randint(0, 3)
  return direccion[indice]
