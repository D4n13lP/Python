from datetime import date
date.today()
print(date.today())
## Empieza el inciso 2
cm = input("Ingrese los cm que desea convertir en M\n")
m = float(cm) / 100
print(float(cm), "cm equivalen a:", float(m), "M")
## Empieza el inciso 3
print("\nEl siguiente programa calcula la distancia que hay entre 2 planetas con respecto al sol\n")
planeta_1 = input("¿A que distancia del sol se encuentra el planeta 1?\n")
planeta_2 = input("¿A que distancia del sol se encuentra el planeta 2?\n")
distancia = float(planeta_1) - float(planeta_2)
if float(distancia) < 0:
    distancia*=(-1)
    print("La distancia que hay entre los 2 planetas es:", float(distancia))
else: 
    print("La distancia que hay entre los 2 planetas es:", float(distancia))
