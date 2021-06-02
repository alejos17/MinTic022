""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#---------------- Zona librerias------------
import smarth_home as sh

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def recibir_datos():
    comando=input("Comando a recibir: ")
    return comando

sh.separar_cadenas(recibir_datos())


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================