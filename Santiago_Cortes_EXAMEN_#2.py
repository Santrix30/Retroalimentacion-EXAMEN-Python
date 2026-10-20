#ejercicio 1

import os

for i in range(2):

    producto = []

    nombre = input("Que va a comprar: ")
    producto.append(nombre)

    try:
        precio = int(input("Que precio tiene: "))
        producto.append(precio)

    except ValueError:
        print("Error, no se ingreso un numero...")
        continue

    tiene_descuento = input("Tiene descuento y = si /n = no: ")

    if tiene_descuento == "y":
        tiene_descuento = True
    elif tiene_descuento == "n":
        tiene_descuento = False
    else:
        print("Error")
        continue

    producto.append(tiene_descuento)

    producto = tuple(producto)
    nombre, precio, tiene_descuento = producto

    if tiene_descuento is True:
        print("Usted cuenta con descuento, ya lo aplicamos\n")

        descuentoA = precio * 0.15
        descuentoB = precio - descuentoA

        print(f"Su total del {nombre} fue de {precio}")
        print(f"Pero ya que tiene descuento le sale en {descuentoB}")

    elif tiene_descuento is False:
        print("Usted no cuenta con descuento\n")
        print(f"Su total del {nombre} fue {precio}")

    os.system("pause")
    os.system("cls")






#ejercicio 2

import os

print("Programa de calificaciones")

calificaciones = (80, 90, 85)
notabuena = 200

total = sum(calificaciones)

print(f"Sus calificaciones fueron de {calificaciones}")

if total >= 270:
    print(f"Excelente nota, saco un {total}")
    os.system("pause")
    os.system("cls")

elif total >= 200:
    print(f"Buena nota, saco un {total}")
    os.system("pause")
    os.system("cls")

else:
    print(f"Una nota insuficiente, saco un {total}")
    print(f"Recuerde, para una nota buena le hace falta {notabuena - total}")
    os.system("pause")
    os.system("cls")



#ejercicio 3

import os

Promedio = 0

temperaturas = []
Frias = []
Templadas = []
Calurosas = []

veces = 4

for i in range(veces):
    temp1 = float(input(f"Digite la {i + 1} temperatura: "))
    temperaturas.append(temp1)

    Promedio = Promedio + temp1

    if temp1 < 20:
        print("Temperatura fria")
        Frias.append(temp1)

    elif temp1 >= 20 and temp1 <= 28:
        print("Temperatura templada")
        Templadas.append(temp1)

    elif temp1 > 28:
        print("Temperatura calurosa")
        Calurosas.append(temp1)

print("Al final se hizo un promedio y unas listas\n")

print("Temperaturas ingresadas:")
print(temperaturas)

print(f"El promedio general es {Promedio / veces} \n")

print("Lista de temperaturas frias:")
print(Frias)

print("Lista de temperaturas templadas:")
print(Templadas)

print("Lista de temperaturas calurosas:")
print(Calurosas)

os.system("pause")
os.system("cls")