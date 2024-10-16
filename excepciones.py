# Intentos y excepciones. Manejo de errores en python. Try y except

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)
print_exception_hierarchy(Exception)
    

try:
    divisor=int(input("Ingresa un numero divisor:"))
    result= 100 / divisor
    print(result)

except ZeroDivisionError:
    print("Error: El divisor no puede ser 0")
except ValueError:
    print("Error: Debes introducir un número válido")
    