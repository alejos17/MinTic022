""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres 
    incorpora al modulo calculadora_aritmetica.py
    Alejandro Tamayo
    Mayo 20-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def bienvenida():
    """ 
  Parameters
  ----------
  Se realiza impresión en pantalla de mensaje de bienvenida
  """
    print("Bienvenido al Taller 2, Semana 3 de MicTIC2022")
    print("esta pequeña aplicación intenta resolver el siguiente problema")
    print(" ")
    print("Calculadora SuperAmigable")
    print(" ")
    print("En una sola cadena de texto puedes escribir la operación matematica para ser resuelta")
    print(" ")
    print(" ")
    print("Con los datos que vamos a solicitar a continuación evaluaremos la solución propuesta")
    print(" ")
    print(" ")

def pedir_cadena():
  """ 
  Parameters
  ----------
  Returns
  -------
  a:string
    Se toma lo digitado en el teclado
  """ 
  a=input("Escriba la operación:  ")
  return a

def analizar_cadena(cadena):
   
  """ 
  Parameters
  ----------
  cadena:string
    Contiene la operacion escrita por el usuario
  Returns
  -------
  pn,sn,operador:string
    Retorna primer numero, segundo numero y el operador
  """ 
  cant=len(cadena) #Calcula la cantidad de caracteres en la cadena
  print(" ")
  print(" ")
  print("Cantidad de caracteres: ",cant)
  pn=""   #Iniciacion de variables
  sn=""
  operador=""

  #Primer ciclo para sacar el primer numero y el operador
  for i in range(0,cant):  #Comenzar en 0 e ir hasta la cantidad de la cadena
      if cadena[i].isdigit() or cadena[i]==".":  #Verifica si es numero o signo punto para decimal
          pn+=cadena[i]   #Adiciona a la cadena los numeros encontrados
      elif cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/":  #Si detecta en la cadena los simbolos matematicos entonces lo guarda en operador
          operador=cadena[i]
          break    #Cierra el ciclo porque llego al operador y tiene el primer numero
      else:     #Si se escribe un caracter diferente, imprime mensaje y termina el programa
          print("Simbolo de operador erronero, por favor escriba bien")
          exit()
  
  #Segundo ciclo para sacar el segundo numero el contador i continua donde quedo
  for i in range(i,cant):
      if cadena[i].isdigit() or cadena[i]==".":
          sn+=cadena[i]

  #Si el segundo numero es 0, para la division, imprime error y termina el programa
  if sn=="0" and operador=="/":
      print("El segundo numero no puede ser cero para la división, por favor corregir")
      exit()

  return pn,sn,operador

def calculos(pn,sn,operador):
  """ 
  Parameters
  ----------
  pn,sn,operador:string
    entrega el numero 1, numero 2 y operador
  Returns
  -------
  resultado:float
  msg:string
    Entrega resultado de operación y mensaje de lo realizado
  """ 
  pn=float(pn)   #Conversion a float del primer numero
  sn=float(sn)   #Conversion a float del segundo numero
  if operador=="+":   #Condion para suma, resta, multi, division
      resultado=calc.sumar_numeros(pn,sn)
      msg="suma "
  elif operador=="-":
      resultado=calc.restar_numeros(pn,sn)
      msg="resta "
  elif operador=="*":
      resultado=calc.multiplicar_numeros(pn,sn)
      msg="multiplicación "
  elif operador=="/":
      resultado=calc.dividir_numeros(pn,sn)
      msg="división "
  return resultado,msg

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
bienvenida()  #Mensaje de inicio de programa
cadena=pedir_cadena()  #Solicitud de la cadena con la operación
pn,sn,operador=analizar_cadena(cadena)  #Funcion para descomponer la cadena
resultado,mensaje=calculos(pn,sn,operador) #Funcion para calcular resultado
print(" ")
print(" ")
print("El primer Numero es: ",pn)
print("El segundo Numero es: ",sn)
print("El Operador indicado es: ",operador," ",mensaje)
print("===============================================")
print("El Resultado es la operación es: ",resultado,)
print("===============================================")

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#TODO: Leer cadena de entrada
#num_1,num_2,op= parser_cadena(cadena_entrada)
#TODO: terminar programa 


"""
import re
 
while True:
    entrada = input("Introduce una cadena de calculo : ")
    print("Entrada1: ",entrada)
    #entrada = entrada.replace(" ", "")
    #print("Entrada2: ",entrada)

    if entrada=="0":
        break
 
    valores=re.findall("([0-9]+)([\+\-*\/])?",entrada)
    print(valores)
 
    if valores:
 
        for i in range(0,len(valores)):
            if i==0:
                resultado=int(valores[i][0])
                print("si i=0:  ",resultado)
            else:
                if operacion=="+":
                    resultado=resultado+int(valores[i][0])
                    print("Suma: ",resultado)
                elif operacion=="-":
                    resultado=resultado-int(valores[i][0])
                elif operacion=="*":
                    resultado=resultado*int(valores[i][0])
                elif operacion=="/":
                    resultado=resultado/int(valores[i][0])
 
            operacion=valores[i][1];
 
        print("Resultado: ",resultado)


        #"([0-9]+)([\+\-*\/])?"

"""        