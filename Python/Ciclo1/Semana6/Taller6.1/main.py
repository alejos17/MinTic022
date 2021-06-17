""" Programa lineas de metro
    Programa para el manejo de conexiones entre estaciones de metro
    incorpora al modulo rostros.py
    Oscar Franco-Bedoya
    Junio 2-2021 """

#---------------- Zona librerias------------
import metro as mt
import numpy as np

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

estaciones=int(input("Cuantas estaciones son?: "))
matriz=np.eye(estaciones)  #con eye me pone cada estacion en la matriz
print(len(matriz))

for x in range(0,len(matriz)):
    for i in range (0,len(matriz)):
        if i<len(matriz)-1:
            if x==i:
                if 0<=i<=8:
                    matriz[x-1][i]=1
                    matriz[x][i+1]=1
                    if 0<=i<=6:
                        matriz[x][i-1]=1
            if x==6 and i==6:
                matriz[x][i+1]=1
            if x==8 and i==8:
                matriz[x-7][i]=1
                matriz[x][i-7]=1
#TODO Continuar las conexiones del ejercicio.


print(matriz)


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================