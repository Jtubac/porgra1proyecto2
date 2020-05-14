#Programa para jugar piedra papel o tijera para despues consultar el historial.
import random 
from random import choice #importamos las librerias correspondientes
from collections import deque #importamos el tipo de dato (Pilas)

#Creamos nuestra pila 
acontecimientos = deque()

def Componentes_juego():
    
    Resultados = 0
    Listado = ["Piedra", "Papel", "Tijera"] #creamos lista de las opciones que tendrá el programa
    Acumulador = (choice((Listado)))

    Eleccion = input("Escoge una opción Piedra, Papel, Tijera: ")
    
    if Eleccion not in Listado:
        #En caso de no elegir un opcion válida se imprime en pantalla en siguiente mensaje
        print ("Tu opción es incorrecta, Por favor vuelve a intentarlo")
    
    if Eleccion == Acumulador:
        Resultados = 0
        print("Empate")

#Creamos los if para el desarrollo del juego
    if (Eleccion == "Piedra"):
        if (Acumulador == "Papel"):
            Resultados = 2
            print("computadora: ", Acumulador)
            print("Gana Computadora")
        elif (Acumulador == "Tijera"):
            Resultados = 1
            print("Humano: Piedra")
            print("Gana Humano")

    if (Eleccion == "Papel"):
        if (Acumulador == "Tijera"):
            Resultados = 2
            print("computadora: ", Acumulador)
            print("Gana Computadora")
        elif (Acumulador == "Piedra"):
            Resultados = 1
            print("Humano: Papel")
            print("Gana Humano")

    if (Eleccion == "Tijera"):
        if (Acumulador == "Piedra"):
            Resultados = 2
            print("computadora: ", Acumulador)
            print("Gana Computadora")
        elif (Acumulador == "Papel"):
            Resultados = 1
            print("Humano: Tijera")
            print("Gana Humano")
    #Agregamos los elementos usando append
    acontecimientos.append((Eleccion))
    acontecimientos.append((Acumulador))
    acontecimientos.append((choice(Listado)))
    return Resultados

#Usamos la estructura def para crear un contador
def covid():
    Humano = 0
    Servidor = 0
    h = False
    while h==False:
        Resultados = Componentes_juego()
        if Resultados == 1:
            Humano += 1
        elif Resultados == 2:
            Servidor += 1
        print ("Estadistícas: Computadora:  ", Servidor, "Humano:  ", Humano) #imprimimos en pantalla los resultados del contador
        Variante=input("Para seguir jugando [y] para ver el Historial [h] : y/h: ")
        if(Variante == "h"):
            print("El Historial es:")
            h = True
            
covid()

#Mostramos el historial con una estructura if
if len (acontecimientos) > 0 :
    ultimo_registro  =  acontecimientos . pop ()
    #Imprimimos resultados en pantalla
    print ( f"Ultima elección: { ultimo_registro } " )
    print ( f"Humano [] Computadora []: { acontecimientos } " ) #Del lado Izquierdo muestra la opcion del Humano y de la Derecha la de la Computadora
    





    
 