#Aprendiendo funciones def haciendo una calculadora. 

def add(a,b):
    return a+b
def subtrack(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator():

# Manejando el bucle while con su terminacion break, el bucle if, elif, y else. Sistema de opciones.

    while True:
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicación")
        print("4.División")
        

        option = input("Ingrese su opción:(1,2,3,4,5):")

        if option == "5":
            print("saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:

            num1 = float(input("ingrese el primer numero"))
            num2 = float(input("ingrese el segundo numero"))

        if option == "1":
            print("la suma es:", add(num1,num2))
        elif option == "2":
            print("la resta es:", subtrack(num1,num2))
        elif option =="3":
            print("la multiplicación es:", multiply(num1,num2))
        elif option =="4":
            print("la división es:", divide(num1,num2))
        else: 
            print("opción no válida, intenta de nuevo")
calculator()

