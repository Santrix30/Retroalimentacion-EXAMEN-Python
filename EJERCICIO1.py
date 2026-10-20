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