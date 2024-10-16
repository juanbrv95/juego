fruits=['Manzana','Pera','Uva','limon']

for fruit in fruits:
    print(fruit)
    if fruit=='Manzana':
        print('Manzana encontrada')

x= 0

# El bucle while es una condicion que se repite infinitas veces. Se utiliza el metodo "break" para detener el bucle.

while x<=3:
    if x == 2:
        break
    print(x)
    x+=2
    

limit=15

odd_itter=iter(range(1,limit+1,2))

for num in odd_itter:
    print(num)