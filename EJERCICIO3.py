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

print("\nAl final se hizo un promedio y unas listas")

print("Temperaturas ingresadas:")
print(temperaturas)

print(f"El promedio general es {Promedio / veces} °C\n")

print("Lista de temperaturas frias:")
print(Frias)

print("Lista de temperaturas templadas:")
print(Templadas)

print("Lista de temperaturas calurosas:")
print(Calurosas)

os.system("pause")
os.system("cls")