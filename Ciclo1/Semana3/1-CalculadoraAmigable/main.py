""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Alejandro Tamayo
    Mayo 19-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular dicvisión: (3)")
  print("==================================================")
   
  opcion = input()
  return opcion

def pedir_numeros():
  """ 
  Parameters
  ----------
  Returns
  -------
  a,b,float
     valores de los numeros a sumar
  """ 
  q=1  #Bandera para bucle de pedido de segundo numero por si es igual o menor a cero
  print(" ")
  print(" ")
  a=float(input("Por favor escribir el numero 1:  "))
  while q==1:  #Bucle para repetir solicitud de numero dos hasta que el usuario coloque el correcto
    b=float(input("Por favor escribir el numero 2:  "))
    if b<=0:
      print("Error, el numero dos, no puede ser numero menor o igual a cero, cambielo")
    else:
      q=0
  return a,b

def operaciones(operacion,numero_uno,numero_dos):
  """ 
  Parameters
  ----------
  operacion:string
  numero_uno,numero_dos:float
     valores de tipo de operación, numeros a operar
  Returns
  -------
  s,r,m,d:float
  msg:string
     valores del resultado de la operación y el mensaje que se realiza
  """ 
  if operacion=="1":
    s=calc.sumar_numeros(numero_uno,numero_dos)
    msg="suma"
    return s, msg
  elif operacion=="2":
    r=calc.restar_numeros(numero_uno,numero_dos)
    msg="resta"
    return r, msg
  elif operacion=="3":
    m=calc.multiplicar_numeros(numero_uno,numero_dos)
    msg="multiplicacion"
    return m, msg
  elif operacion=="4":
    d=calc.dividir_numeros(numero_uno,numero_dos)
    msg="division"
    return d, msg


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
opcion=menu()

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
numero_uno,numero_dos=pedir_numeros()
resultado,mensaje=operaciones(opcion,numero_uno,numero_dos)
print(" ")
print(" ")
print("Ha seleccionado la opcion: ",opcion," por tanto se realiza la ",mensaje," de los numeros ",numero_uno," y ",numero_dos)
print(" ")
print("El resultado es: ",resultado)
