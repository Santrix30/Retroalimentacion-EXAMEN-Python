#ejercicio 2
import os

print("Programa de calificaciones")

calificaciones = (10, 10, 10)
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