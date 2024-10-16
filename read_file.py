#Leer un archivo linea por linea

"""with open('escritura.txt','r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Lee todas las lineas en una lista

with open('escritura.txt','r') as file:
    lines = file.readlines()
    print(lines)

