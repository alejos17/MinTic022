""" Reto 3 Priorizacion de Vacunas  #
    incorpora al modulo etapa_vacuna.py
    Alejandro Tamayo
    Mayo 22-2021 """
#---------------- Zona librerias------------
import etapa_vacuna as ev
from datetime import datetime
from dateutil.relativedelta import relativedelta

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def bienvenida():
    """ 
    Parameters
    ----------
    Se realiza impresión en pantalla de mensaje de bienvenida
    """
    print("Bienvenido al Reto 3, Semana 3 de MicTIC2022")
    print("esta pequeña aplicación intenta resolver el siguiente problema\n")
    print("Priorización de Vacunación\n")
    print("Según una serie de preguntas, se le indicará su prioridad de vacunación según las etapas creadas por el Ministerio de Salud de Colombia en el Plan Nacional de Vacunación\n\n")
    print("Con los datos que vamos a solicitar a continuación evaluaremos la solución propuesta\n\n\n")

def solicitud_datos():
    """ 
    Parameters
    ----------
    Returns
    -------
    nombre,fecha_nac,edad,correo,ts,th,th1,teb,td,tir,tvih,tc,tb,te,ta,to,tls,tpl,tp,tpol,tam,tre,tbc,tcr,tdc,tca,tba,tpt,tav,tec:string
            Toma las respuestas por teclado
    """
    print("Por favor, ayudenos respondiendo las siguientes preguntas")
    print("Respueta S para Sí  y  N para No\n")
    print("===================================================================================")
    nombre=input("Nombre completo: ")
    fecha_nac=datetime.strptime(input("Fecha de Nacimiento  d/m/a: "), "%d/%m/%Y")
    #Calcular la edad con la funcion relativedelta y la fecha de nacimiento.
    edad = relativedelta(datetime.now(), fecha_nac)
    #Se solicita solo los años, ya que relativedelta entrega meses y dias
    edad=edad.years
    print("Usted tiene: ",edad," años")
    correo=input("Correo Electrónico: ") 
    while "@" not in correo:  #Si el usuario no coloca ninguna arroba, quiere decir que el correo esta mal escrito, por lo que entra en bucle solicitando al usuario el correo correctamente.
      print("El correo no tiene el formato correcto, intente de nuevo")
      correo=input("Correo Electrónico: ")
    #Solicitud de cada pregunta en forma de variable
    ts=input("Es usted médico o enfermera?: ")
    ts=validar_datos(ts)  #Se envia lo respondido por el usuario para la funcion validar_datos
    th=input("Trabaja actualmente en un área COVID-19?: ")
    th=validar_datos(th)
    th1=input("Trabaja actualmente en un Hospital?: ")
    th1=validar_datos(th1)
    print("===================================================================================")
    print("En la siguiente sección evaluaremos si tiene alguna enfermedad base o comorbilidades")
    teb=input("Sufre de alguna enfermedad base?: ")
    teb=validar_datos(teb)
    if teb=="s" or teb=="S":  #Se valida si en la pregunta de enfermedad base es SI
        td=input("Diabetes?: ")  #Si responde NO, entonces se omiten las preguntas 
        td=validar_datos(td)
        tir=input("Insuficiencia Renal?: ")
        tir=validar_datos(tir)
        tvih=input("VIH?: ")
        tvih=validar_datos(tvih)
        tc=input("Cancer?: ")
        tc=validar_datos(tc)
        tb=input("Tuberculosis?: ")
        tb=validar_datos(tb)
        te=input("EPOC?: ")
        te=validar_datos(te)
        ta=input("ASMA?: ")
        ta=validar_datos(ta)
        to=input("Obesidad?: ")
        to=validar_datos(to)
        tls=input("Esta en lista de espera para trasplantes?: ")
        tls=validar_datos(tls)
        tpl=input("Es paciente Postrasplante?: ")
        tpl=validar_datos(tpl)
    else:                       #Se omiten preguntas pero se inicializan las variables 
        td=""                   #en blanco
        tir=""
        tvih=""
        tc=""
        tb=""
        te=""
        ta=""
        to=""
        tls=""
        tpl=""
    print("===================================================================================")
    #En estas 3 preguntas: Si es profesor, no es policia ni trabaja con adultos mayores
    #Si es policia, no es profesor ni trabaja con adultos mayores
    #Si trabaja con adultos mayores, no es profesor ni es policia
    tp=input("Es usted profesor?: ")
    tp=validar_datos(tp)
    tpol=""
    tam=""
    if tp=="n" or tp=="N":
        tpol=input("Es usted policía?: ")
        tpol=validar_datos(tpol)
        tam=""
        if tpol=="n" or tpol=="N":
            tam=input("Trabaja usted cuidando adultos mayores?: ")
            tam=validar_datos(tam)
    print("===================================================================================")
    #Se pregunta inicialmente si tiene algún rol especial, si es afirmativo pregunta que tipo de rol es, si no omite las preguntas.
    tre=input("Tiene usted algún rol especial?: ")
    tre=validar_datos(tre)
    if tre=="s" or tre=="S":
        tbc=input("Pertenece a los Bomberos de Colombia?: ")
        tbc=validar_datos(tbc)
        tcr=input("Pertenece a la Cruz Roja Colombiana?: ")
        tcr=validar_datos(tcr)
        tdc=input("Pertenece a la Defensa Civil?: ")
        tdc=validar_datos(tdc)
        tca=input("Es Controlador Aereo?: ")
        tca=validar_datos(tca)
        tba=input("es Bombero Aeronautico?: ")
        tba=validar_datos(tba)
        tpt=input("Es Piloto?: ")
        tpt=validar_datos(tpt)
        tav=input("Es Auxiliar de Vuelo?: ")
        tav=validar_datos(tav)
        tec=input("Es una persona privada de su libertad?: ")
        tec=validar_datos(tec)
    else:       #Si se omiten las preguntas se inicializan variables en blanco
        tbc=""
        tcr=""
        tdc=""
        tca=""
        tba=""
        tba=""
        tpt=""
        tav=""
        tec=""
    print("===================================================================================\n")
    return nombre,fecha_nac,edad,correo,ts,th,th1,teb,td,tir,tvih,tc,tb,te,ta,to,tls,tpl,tp,tpol,tam,tre,tbc,tcr,tdc,tca,tba,tpt,tav,tec

def validar_datos(d):
    """ 
    Parameters
    ----------
    d:string
        ingresa la cadena con la respuesta del usuario
    Returns
    -------
    d:string
        Se entrega como respuesta 's' o 'n' minusculas
    """
    #Si el usuario contesta S o N  simplemente se deja en minuscula y se devuelve
    if d=="s" or d=="S" or d=="n" or d=="N":
        d=d.lower()   #Cambio a minuscula
        return d
    else:       #Si la respuesta no es S o N, entonces se entra en bucle para que conteste 
        while d!="s" and d!="S" and d!="n" and d!="N":
            d=input("*** Respuesta no conocida, 's' para Si, 'n' para No ***: ")
    d=d.lower()     #Cambio a minuscula
    return d


def mensajes(etapa,msg,nombre,fecha_nac,edad,correo):
    """ 
    Parameters
    ----------
    etapa,msg,nombre,fecha_nac,edad,correo:string
        Entran los datos para desplegar los mensajes de respuesta
    Returns
    -------
    """
    print("Buen Dia ",nombre,"\n")
    print("Sus datos: ")
    print("Fecha de Nacimiento: ",fecha_nac)
    print("Edad: ",edad," años")
    print("Correo: ",correo,"\n")
    print("**** ",msg," ****\n")
    print("Descripción: ",etapa,"\n")
    print("========================================================================")
#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================
#Inicio de programa, desplegando mensajes
bienvenida()
#Comienza solicitud de datos
nombre,fecha_nac,edad,correo,ts,th,th1,teb,td,tir,tvih,tc,tb,te,ta,to,tls,tpl,tp,tpol,tam,tre,tbc,tcr,tdc,tca,tba,tpt,tav,tec=solicitud_datos()
#Llama funcion etapas para clasificar según las variables
etapa,msg=ev.etapas(nombre,fecha_nac,edad,correo,ts,th,th1,teb,td,tir,tvih,tc,tb,te,ta,to,tls,tpl,tp,tpol,tam,tre,tbc,tcr,tdc,tca,tba,tpt,tav,tec)
#Funcion para desplegar mensaje de respuesta
mensajes(etapa,msg,nombre,fecha_nac,edad,correo)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


"""
while "@" not in correo:
      print("El correo no tiene el formato correcto, intente de nuevo")
      correo=input("Correo Electrónico: ")

  while b==1:
      ts=input("Es usted médico o enfermera?: ")
   ts,b=validar_datos(ts)
      print(ts)
  if ts=="S" or ts=="s":
      b=1
      while b==1:
        th=input("Trabaja actualmente en un hospital?: ")
        th=validar_datos(th)
        print(th)

  print(ts)

  return 

def validar_datos(d):
    if d=="s" or d=="S" or d=="n" or d=="N":
        b=0
        return d, b
    else:
        msg="*** Respuesta no conocida, por favor intente de nuevo ***"
        b=1
        return msg

"""