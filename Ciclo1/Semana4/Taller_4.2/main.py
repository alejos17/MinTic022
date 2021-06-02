import funciones_listas as fl

def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido a la Miscelanea de ejercicios Taller 4.2")
    print("Seleccione el algoritmo a verificar:\n")
    print("1. Suma Acumulativa")
    print("2. Traductor Pig Latin")
    print("3. Vitamina A")
    print("4. ")
    print("5. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Bandera para entar al bucle del menú
flag=1
while flag==1:
    op=menu()
    if op==1: 
        print(" ")
        print("*** Suma Acumulada ***")
        lista_n=input("Indique los numeros separados por comas: ")
        suma_ac=fl.suma_acumulativa(lista_n)
        print("La Suma acumulada es: ",suma_ac)
    elif op==2: 
        print(" ")
        print("*** Traductor Pig Latin ***\n")
        fl.traductor_pig_latin()
    elif op==3: 
        print(" ")
        print("*** Frutas con Vitamina A ***\n")
        fl.identificador_frutas()
    elif op==4: 
        print(" ")
        print("*** Frase Palindroma ***\n")
        fl.son_palindromos()
    elif op==5: exit()
    else: print("Opción no valida, intente de nuevo")

