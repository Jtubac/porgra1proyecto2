####empieza el programa
from tkinter import * 
from tkinter import ttk
raiz = Tk()
raiz.geometry('300x200')
raiz.configure(bg = 'beige')
raiz.title('Programa Venta Lavado')
import json
print ("****Bienvenido al Programa*****")
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
tipo_vehiculo=input('Ingrese el tipo de vehiculo: ')
print()

######## tipo de Cliente
tipo_cliente = input('Ingrese el [1] si Estandar, ingrese [2] si es Miembro: ')
if tipo_cliente=='1':
    cli='Estandar'
    print ("Estandar")
elif tipo_cliente=='2':
    cli='Miembro'
    print ("Miembro")
print()
######## tipo de dias 
dias = input ('Ingrese [1] si es fin de semana y [2] si es dia normal ')
if dias =='1':
    dia='True'
    print ("fin de Semana")
elif dias=='2':
    dia='False'
    print("Dia normal")
######### ingreso de precio
print('<<<El precio a para es Q 15 motocicleta, Q 30 Automovil, 50 Camion>>>')
precio = input('Ingrese el precio de lavado: ')
if dias=='2' and tipo_cliente=='2':
    descuento:float
    total:float
    descuento= (float(precio))*0.20
    total=(float(precio)-descuento)
else:
    total:float
    descuento:float   
    descuento=(float(precio))*0.10
    total=(float(precio)-descuento)
if dias =='1' and tipo_cliente=='1':
    total= precio
    descuento=(float(precio))*0
############Impresion de Datos
print()
print('El tipo de vechiculo es: ', tipo_vehiculo)
print('El tipo de cliente es: ', cli)
print('Es Fin de semana: ', dia)
print('El descuento es: ', descuento)
print('El Precio a pagar es: ', total)

print()
####JSON
datos = [
    {
    'Tipo': tipo_vehiculo,
    'Precio':precio,
    'Cliente': cli,
    'Fin de Semana': dia,
    'Descuento':descuento,
    'Total':total
}
]
#####exportado de datos al archivo JSON
with open('datos.json', 'w') as file:
    json.dump(datos, file)
    print('datos exportados con exito')
    print()
    ler=input('Ingrese "1" si desea leer datos, y "2" para no leer los datos: ')
###### Obtener datos del archivo JSON
if ler=='1':
    print ('Datos obtenidos con exito del archivo JSON')
    print()
    with open('datos.json', 'r') as file:
        data = json.load(file)
    print(data)
elif ler=="2": 
    print('Datos no leidos del archivos')
    print()
print("<<<<<< Gracias por Visitarnos >>>>>>")

