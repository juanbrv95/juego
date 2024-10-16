# nombre = "juan"

#while True: 
#    nombre = input("ingresa tu nombre:")
#   if nombre != "juan":
      

telefono = "123-456-789"

for i in telefono:
    if i == "-":
        continue
    print(i, end="")


for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)