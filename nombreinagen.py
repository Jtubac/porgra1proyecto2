import os
import json

archivo=[]
nuevo=[]
archivo="lobo.jpg"
nuevo="ejemplo_1.jpg"
os.rename(archivo, nuevo)
print([archivo], [nuevo])

archivo="tienda.jpg"
nuevo="ejemplo_2.jpg"
os.rename(archivo, nuevo)
print([archivo], [nuevo])

archivo="sonic.jpg"
nuevo="ejemplo_3.jpg"
os.rename(archivo, nuevo)
print([archivo], [nuevo])
print()
print("Ha realizado el cambio de nombre a los archivos")
