# Uso del generador e iteracion de los numeros pares e impares
def num_par(limit):
    a=1
    while a< limit+1:
        yield a
        a=a+2
    for num in num_par(10):
        print(num)
        
