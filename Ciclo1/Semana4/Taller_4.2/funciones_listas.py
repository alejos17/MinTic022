""" Modulo Listas
    Funciones para practicas con listas
    Alejandro Tamayo
    Mayo 29-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def suma_acumulativa(lista_n):
    """ 
    Parameters
    ----------
    lista_n:string
        Cadena con valores numericos separados por comas
    Returns
    -------
    listacum:Lista
        Entrega la lista de numeros con la suma acumulada
    """
    lista_n=eval(lista_n)  #Se utiliza la funcion para crear una lista
    print("La lista indicada es: ",lista_n)  #Imprime lista en pantalla
    listacum=[]     #Se inicializa la lista para acumular
    a=lista_n[0]    #Se toma el primer valor de la lista enviada
    listacum.append(a)  #Se agrega a lista acumulada
    for x in range((len(lista_n))-1):  #Recorrido de la lista
        if x<(len(lista_n))-1:      #Condicion para no salir del rango 
            a=a+lista_n[x+1]  #Suma el numero anterior al nuevo en la posicion
        listacum.append(a)  #Se agrega el valor a la lista de acumulado
    return listacum

def traductor_pig_latin():
    vocales=["a","e","i","o","u"]
    palabras_ingles=[]
    palabras_pig=[]
    msg=1

    while msg==1:
        p=input("Escriba las palabras para agregar a la lista a traducir: ")
        palabras_ingles.append(p)
        print(" ")
        msg=int(input("Desea agregar otra palabra?: 1.Si  2.No:  "))
        print(" ")

    print("")
    print("Lista de palabras ingresadas en Ingles: ")
    print(palabras_ingles)
    print("===========================================================\n")

    for element in palabras_ingles:
        a=element
        c=a[0:1:]
        if c in vocales:
            b=a+"yay"
            palabras_pig.append(b)
        else:
            a=a.lstrip(a[0])
            a=a+c+"ay"
            palabras_pig.append(a)
    
    print("Lista de palabras traducidas a Pig Latin: ")        
    print(palabras_pig)
    print("===========================================================\n")
    return

def identificador_frutas():
    frutas=[]
    resultado=[]
    msg=1

    while msg==1:
        p=input("Por favor escriba las frutas: ")
        frutas.append(p)
        print(" ")
        msg=int(input("Desea agregar otra fruta?: 1.Si  2.No:  "))
        print(" ")

    print("===========================================================\n")
    print(" ")
    print("Las frutas ingresadas son:\n")
    print(frutas)    

    for element in frutas:
        a=element
        if "a" in a:
            resultado.append(a)

    print("===========================================================\n")
    print(" ")
    print("Las frutas que tienen la letra A y por tanto Vitamia A son:\n")
    print(resultado)
    print("===========================================================\n")
    return 

def son_palindromos():
    frase1=input("Escriba la primera frase: ")
    frase2=input("Escriba la segunda frase: ")

    frase1i=frase1[::-1]
    frase2i=frase2[::-1]

    print(frase1)
    print(frase1i)
    print(" ")
    print(" ")
    print(frase2)
    print(frase2i)
    return
