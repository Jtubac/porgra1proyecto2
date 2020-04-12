print("****Bienvenido al Programa")

basededatos = []

for pe in range(2):
    persona = {}
    modelo=input("Ingrese el modelo del vehiculo: ")
    edad = input('Ingrese la edad: ')
    nombre = input ('Ingrese el nombre: ')     
    persona['modelo']=modelo
    persona['nombre'] = nombre
    persona['edad']=edad
    basededatos.append(persona)

if pe <=2:
     print("<<<<<< Gracias por Visitarnos >>>>>>")
