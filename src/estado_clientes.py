# Importar el modulo csv para leer el archivo CSV
import csv

# Abrir el archivo clientes.csv con codificaicon UTF-8
with open("datos/clientes.csv", encoding= "utf-8") as archivo:
    # DictReader lee cada fila del csv como un diccionario utilizando los encabezados como claves
    clientes = list(csv.DictReader(archivo))

# Creo lista vacia donde guardo los nombres de quienes siguen

siguen = []

# Recorro la lista y en cada vuelta verifico si sigue o no

for cliente in clientes:
    if cliente["abandono"] == "0":
        siguen.append(cliente["nombre"])

# Compresion de listas, sintaxis compacta para construir una lista a partir del recorrido y opcionalmente el filtrado o la transformacion de otra coleccion

abandonan = [ cliente["nombre"] for cliente in clientes if cliente["abandono"] == "1"]

print("Clientes que siguen:", ", ".join(siguen))
print("Clientes que abandonan:", ", ".join(abandonan))