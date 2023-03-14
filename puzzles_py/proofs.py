"""
for number in range(10):
    if number == 5:
        #num= 4 + number
        continue
    print(number, end=' ')

for number in range(100):
    if number == 20:
        break
    print(number, end=' ')

"""
"""
grade = 87
if not grade == 87:
    print('The next grade is', grade)

### Another way to write not

grade = 87
if grade != 90:
    print('The next grade iS', grade)
"""

### DEFS!!!!
"""
number = 12
def square(number):
##    Calculate the square of number
    return number ** 2

print(square(number))

val1 = 50
val2 = 20
val3 = 100

def maximum(val1, val2, val3):
##   Return the maximum of three values
    max_val = val1
    if val2 > max_val:
        max_val = val2
    if val3 > max_val:
        max_val = val3
    return max_val

print(maximum(val1, val2, val3))

m = max('yellow', 'red', 'orange', 'blue', 'green')
print(m)
"""

"""Se creará un juego de dados llamados Craps"""
import random

"""
1. se crea la función para poder generar los valores de los dados
"""
def tiradas():
    """tirar el dado 2 veces, se va a regresar los valores obtenidos como una tupla"""
    cara1 = random.randrange(1, 7)
    cara2 = random.randrange(1, 7)
    return (cara1, cara2) # se guardan las caras en una tupla
    
def numero_dado(valor): ###tengo duda porque usa valor dentro de los parentesis
    """Despliega una tirada de los dos dados"""
    cara1, cara2 = valor # pasa el valor de la tupla en las variables cara1 y cara2
    print(f'Tirada del jugador {cara1} + {cara2} = {sum(valor)}')
#    print(cara1) ###comprobaciones de lo anterior

###Comienza a ejecutar el código
valor_dado = tiradas() ### primera tirada, aqui guarda los valo
print('corroborando', valor_dado) ## Podemos comprobarlo con este print
numero_dado(valor_dado) 
#print(numero_dado(valor_dado))

##se va a determinar el estatus del juego y su puntaje basandose en la primera tirada
suma_dado = sum(valor_dado)

if suma_dado in (7, 11): # gana
    game_status = 'GANAAAA'
elif suma_dado in (2, 3, 12): # perder
    game_status = 'PERDEDOR'
else: # si no cumple los anteriores condicionales usa este para crear más tiradas dentro de un while
    game_status = 'CONTINUE'
    puntaje = suma_dado
    print('Puntooooooooooooooo de la primera tirada', puntaje)

#### hasta que gane o pierda saldremos del while
while game_status == 'CONTINUE': ###este estatus viene de arriba, el cual ayudará a generar el loop casi eterno
    valor_dado = tiradas() #como se dará otra oportunidad se tendrá que volver a empezar, por eso se agregar esta línea
    #print(valor_dado)
    numero_dado(valor_dado)
    #print(valor_dado)
    suma_dado = sum(valor_dado)
    #print(puntaje)
    if suma_dado == puntaje: ##para ganar debe de ser el mismo resultado de la suma con la del puntaje(punto)
        game_status = 'WON'
    elif suma_dado == 7: 
        game_status = 'LOST'
    
    print(game_status)

### Se da el resultado
if game_status == 'WON':
    print('Por fiiiiiiiin ganaste, sistaaaaaaaa',valor_dado)
else:
    print('Chaleeeeee, continuas reinaaaaaaaa',valor_dado)
