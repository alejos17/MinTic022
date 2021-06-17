""" Modulo Ciclos
    Funciones para practicas con ciclos
    Alejandro Tamayo
    Mayo 29-2021 """

import math as m

# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_caida_libre():
  print("Hola")
  altura=float(input("Por favor indique la altura en metros: "))
  gravedad=float(9.8)
  tiempo = m.sqrt((2*altura)/gravedad)
  tiempo2=tiempo
  print("El tiempo del recorrido total es: ",tiempo)
  tiempo=round(tiempo,2)

  print("Aproximación de tiempo es: ",tiempo,"\n\n")

  while tiempo>=0:
    d=(altura)-(1/2)*gravedad*(tiempo**2)
    d=round(d,2)
    print("A ",(tiempo2-tiempo)," segundos ha reocorrido : ",d," metros")
    tiempo-=1
    tiempo=round(tiempo,2)
  return

def generador_generaciones():
  listapersonas=[]
  listageneraciones=[]
  x=0
  b=0
  generacion=int(input("Por afavor indique la generacion: "))

  while generacion<0:
    print("Error, no se puede colocar generaciones negativas")
    print("Intente de nuevo")
    generacion=int(input("Por afavor indique la generacion: "))

  if generacion==0:
    listapersonas.append(1)
    listageneraciones.append(0)
    b+=listapersonas[x]   
  else:
    for x in range(generacion):
        listageneraciones.append(x)
        if listageneraciones[x]==0:
            listapersonas.append(1)
            b+=listapersonas[x]
        elif listageneraciones[x]==1:
            listapersonas.append(2)
            b+=listapersonas[x]
        else:
            a=listapersonas[x-1]
            listapersonas.append(a*2)
            b+=listapersonas[x]

  #Para imprimir mensaje
  for i in listageneraciones:
    print("Para la generación ",listageneraciones[i],"son",listapersonas[i],"personas")
  
  #print(listageneraciones)
  #print(listapersonas)
  print("El total de personas es de: ",b)
  return

def constructor_triangulos():
  x=0   #Inicio de contador
  #Se solicita cantidad de pisos y se resta 1 para que sea real, porque comienza en 0 la posicion
  cantidad=int(input("Por favor indicar el numero de pisos: "))-1

  a=[1]    #Lista inicia con valor 1
  print(a)    #Se imprime el primer piso  [1]
  for x in range(cantidad):   #Se recorre según la cantidad indicada
    a[0]=a[-1]+1  #Incrementa la posicion a[0], según el ultimo numero
    
    #Recorre toda la lista y suma la posicion en base a a[0]
    for index in range(len(a)):
        a[index]=a[0]+index
    
    #agrega un valor adicional a la lista con numero más alto
    a.append(a[-1]+1)
    print(a)
  return

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"