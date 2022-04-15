#Menu example from https://www.discoduroderoer.es/crear-un-menu-de-opciones-en-consola-en-python/
import logging 

logging.basicConfig(
    filename='log.txt',
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

def pedir_numero_entero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            logging.exception('Error, introduce un numero entero')
    return num
 

pilas = list()

def pedir_caracter():
    caracter = ''
    correcto=False

    while(not correcto):
        try:
            caracter = input("Introduce un caracter: ")
            if len(caracter) > 1:
                raise ValueError()
            correcto=True
        except ValueError:
            logging.exception('Error, introduce un caracter')
    return caracter

def nueva_pila():
    salir = False
    opcion = 0
    
    pila = []

    while not salir:
        

        print("Tu pila es:", pila)

        print ("1. Apilar caracter")
        print ("2. Desapilar")
        print ("0. Salir")
        
        print ("Elige una opcion")
    
        opcion = pedir_numero_entero()
    
        if opcion == 1:
            print ("Opcion 1: Apilar caracter")
            caracter = pedir_caracter()
            pila.append(caracter)#in function to push
        elif opcion == 2:
            print ("Opcion 2: Desapilar")
            pila.pop()
        elif opcion == 0:
            salir = True
        else:
            print ("Debes introducir un numero entre 1 y 2 o 0")
    pilas.append(pila)
    logging.info("Pila creada \n")

def seleccion_de_pila():
    while True:
        try:
            opcion = pedir_numero_entero()
            if (opcion < len(pilas) +1 and opcion != 0):
                break
            else: 
                raise ValueError
        except ValueError:
            logging.exception("Introduce un numero valido de la pila a comparar")
    return opcion

def comparar_pilas(p1,p2):
    if len(p1) != len(p2):
        return False
    else:
        for i in range(len(p1)):
            if p1[i] != p2[i]:
                return False
        return True

def comparar_menu():
    salir = False
    while not salir:
        

        print("Las pilas almacenadas son:")

        contador = 0
        for i in pilas:
            contador = contador + 1
            texto = str(contador)+". "+"["
            for j in i:
                texto = texto + "'"+j+"'"
            texto = texto + "]"
            print(texto)
        
        print ("Elige la primera opcion a comparar")
        opcion1 = seleccion_de_pila()
        print ("Elige la segunda opcion a comparar")
        opcion2 = seleccion_de_pila()

        if comparar_pilas(pilas[opcion1-1], pilas[opcion2-1]):
            print("Las secuencias de caracteres son iguales")
        else: 
            print("Las secuencias de caracteres son distintas")
        
        print("Elija que opcion seguir:")

        print ("1. Hacer otra comparacion")
        print ("0. Salir")


        opcion = pedir_numero_entero()
    
        if opcion == 1:
            print ("Opcion 1: Hacer otra comparacion")
        elif opcion == 0:
            salir = True
        else:
            print("Debes introducir un numero puede ser 1 o 0")
    logging.info("Se han comparado secuencias. \n")

def main():
    salir = False
    opcion = 0
    
    print("Bienvenido a este almacenador de caracteres")
    print("¿Que desea hacer? \n")

    while not salir:
    
        print ("1. Apilar nueva secuencia de caracteres")
        print ("2. Comparar secuencias")
        print ("0. Salir \n")
        
        print ("Elige una opcion")
    
        opcion = pedir_numero_entero()
    
        if opcion == 1:
            print ("Opcion 1: Apilar nueva secuencia de caracteres")
            nueva_pila()
        elif opcion == 2:
            print ("Opcion 2: Comparar secuencias")
            comparar_menu()
        elif opcion == 0:
            salir = True
        else:
            print("Debes introducir un numero entre 1 y 2 o 0")
    
    logging.info("Fin")

main()
