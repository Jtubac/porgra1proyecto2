#importar el tipo para utilizar pilas y colas
from collections import deque
import json
import sys

print('1) Desea agregar un elemeto a la cola\n')
print('2) Imprimir\n')
print('3) Salir\n')

let=input('<<<<<Seleccione una de las opciones>>>>>\n')
# esta opcion permite escribir el nombre el archivo para agregar a la cola
if let=='1':
    cola = deque()
    nombrearchivo=input('Escriba el nombre del archivo: ')
    print("el archivo es:", nombrearchivo)
  
    cola.append(nombrearchivo)
    print(f'Cola de impresion: {cola}')
    print('########')

    while len(cola)>0:
        siguinte_elemento = cola.popleft()

        #print(f'Siguiente elemento{siguiente_elemento}')
        #print(f'Cola de Impresion: {cola}')
        #print ('#####')

elif let=='2':
        print('Se seleccionaron los archivos')
        #definir la cola
        cola = deque ()
        #agregar elementos
        cola.append('archivos01.txt')
        cola.append('archivos02.txt')
        cola.append('archivos03.txt')
        
        print(f'Cola de Impresion: {cola}')
        print('######')
        
        while len(cola) > 0:
        # extraer el primer docuemto en la cola
            siguiente_elemento = cola.popleft()

            print(f'Siguiente elemento: {siguiente_elemento}')
            print(f'Cola de impresion: {cola}')
            print ('######')

elif let=='3':
    sys.exit('Se cerro el programa con exito')

    
'''
#definir la cola 
cola = deque ()

#agregar elementos
cola.append('archivos01.txt')
cola.append('archivos02.txt')
cola.append('archivos03.txt')

print(f'Cola de Impresion: {cola}')
print('######')

while len(cola) > 0:
    # extraer el primer docuemto en la cola
    siguiente_elemento = cola.popleft()

    print(f'Siguiente elemento: {siguiente_elemento}')
    print(f'Cola de impresion: {cola}')
    print ('######')


# importar el tipo de dato para utilizar pilas y colas  .......pilas
from collections import deque

# definir la pila
historial = deque()

# usar append para agregar elementos
# es el equivalente al PUSH de una cola normal
historial.append('primera acción')
historial.append('segunda acción')
historial.append('tercera acción')
historial.append('cuarta acción')

print(f"Historial actual {historial}")
print('#################')

while len(historial) > 0:
    # extraer el último elemento utilizando pop
    ultima_acction = historial.pop()

    print(f'Acción más reciente: {ultima_acction}')
    print(f'Historial actual: {historial}')
    print('#################')'''

