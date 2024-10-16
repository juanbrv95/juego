print('Bienvenido a piedra, papel, o tijera')

print('jugador1, ingrese su nombre:')
Player_1= input()
print('jugador2, ingrese su nombre:')
Player_2= input()

print('ingresa que elijes, piedra, papel, o tijera?:')
Player_1=input().lower()
print('ingresa que elijes, piedra, papel o tijera?:')
Player_2=input().lower()

valid_moves=['piedra','papel','tijera']

if Player_1 not in valid_moves or Player_2 not in valid_moves:
    print('no valido', 'ingrese piedra, papel o tijera:')
else:
    if Player_1 == Player_2:
        print('empate')
    elif(Player_1=='piedra' and Player_2=='tijera' or
        Player_1=='papel' and Player_2=='piedra'or
        Player_1=='tijera' and Player_2=='papel'):

        print('player 1 es el ganador:', Player_1)
    else:

        print('player 2 es el ganador:', Player_2)
