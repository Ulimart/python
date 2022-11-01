from ast import Num
from msilib import PID_TITLE
import random

#num = random.random()
#num=num*100
#print(num)

#num= random.randint(0,9)
#print(num)
#num=num*10
#print(num)

#num1= random.randint(0,1000)  ### le estas pidiendo que elija entre el 0 al 1000 un numero
#print(num1)
#num2= random.randint(0,1000)
#print(num2)
#divi=num1/num2
#print(divi)

#num= random.randrange(0,100,5) ### el 3er numero es que marca el intervalo o la diferencia entre el rango que se eligió
#print(num)

#coloretssss= random.choice(["rosa", "lila", "baby blue"])
#print(coloretssss)

#var=random.randint(1,100)
#print(var)

#frutas=random.choice(["fresa","sandía","melón","limón","pera"])
#print(frutas," la fruta más deli")

#selecc=random.choice(["h","t"])
#preg=input("Selecciona si head o tail, 'h' o 't': ")
#if selecc == preg:
#    print("Ganaste un carrito sandwicherooooo!!!")
#else:
#    print("Perdiste!!")
##print("La respuesta elegida por mi fue: ",selecc)  ## segun esto no está bien ya que se debe de decir head or tail
#if selecc == "h":
#    print("La respuesta elegida por mi fue: head")
#elif selecc == "t":
#    print("La respuesta elegida por mi fue: tail")

#selecc=random.randrange(1,5)
#preg=int(input("Elige un numero: "))
#if selecc == preg:
#    print("Muy bien, querido alumno")
#elif selecc > preg:
#    print("Muy pequeño el número")
#    preg=int(input("Vuelve a intentarlo, dame otro numero: "))
#    if selecc == preg:
#        print("Por fiiiiiiiiiiiin, Correcto!!!!")
#    else:
#        print("La cagaste, byeeeeeeeeeeeeeeee!!")
#elif selecc < preg:
#    print("Te pasaste, tu numero es más grande")
#    preg=int(input("Vuelve a intentarlo, dame otro numero: "))
#    if selecc == preg:
#        print("Por fiiiiiiiiiiiin, Correcto!!!!")
#    else:
#        print("La cagaste, byeeeeeeeeeeeeeeee!!")

#num=random.randrange(1,10)
#preg=int(input("Juguemos, adivina el numero que estoy pensando, dime un numero: "))
#while num != preg:
#    preg=int(input("Te equivocaste, vuelve a intentarlo, escribe otro numero: "))

#num=random.randint(1,10)
#resp=False
#while resp == False:
#    print(num)
#    preg=int(input("Juguemos, adivina el numero que estoy pensando, dime un numero: "))
#    if preg == num:
#        resp = True

#num=random.randint(1,10)
#resp=False
#while resp == False:
##    print(num)
#    preg=int(input("Juguemos, adivina el numero que estoy pensando, dime un numero: "))
#    if preg == num:
#        resp = True
#    else:
#        if preg < num:
#            print("Esta abajo del elegido")
#        else:
#            print("Te pasaste, estas muy arriba")

#cont=0
#for i in range(1,6):
#    num1=random.randint(1,10)
#    num2=random.randint(11,20)
#    print("si tenemos el numero",num1,"y el numero",num2,"cuál sería la respuesta de la suma de ambos?")
#    preg=num1 + num2
#    resp=int(input("primera pregunta, dame la respuesta: "))
#    if preg == resp:
#        cont=cont+1
#        print("respuesta correcta")
#    else:
#        print("respuesta incorrecta")
#print("tus número de respuestas correctas fueron:",cont)

#col=random.choice(["sepia","lila","naranja","beibi blue","hueso"])
#resp=input("elige alguno de los liguentes colores y veamos si adivinas el que yo pensé. Sepia,lila, naranja, beibi blue y hueso: ")
#while resp != col:
#    if col == "sepia":
#        print("Mi doverman Anita su pelo es sepia")
#    elif col == "lila":
#        print("Siempre me han gustado los arreglos florales con lilas")
#    elif col=="naranja":
#        print("mi fruta favvvvvvvvvv es naranja")
#    elif col == "beibi blue":
#        print("dicen que el cielo es beibi blue porque diosito es niño jejejeje")
#    elif col == "hueso":
#        print("el esqueleto humano tienen 220 huesos")
#    resp=input("fallaste, elige otro color: ")
#print("bien hecho, adivinaste")

#### respuesta del libro:

col=random.choice(["sepia","lila","naranja","beibi blue","hueso"])
print("elige alguno de los liguentes colores y veamos si adivinas el que yo pensé. Sepia,lila, naranja, beibi blue y hueso: ")
intentalo= True
while intentalo == True:
    resp = input("Elige el color: ")
    resp=resp.lower()
    if col == resp:
        print("Bien hecho mijamon!!!")
        intentalo = False  #### LO CAMBIA A FALSO PARA DETENER EL WHILE
    else:
        if col == "sepia":
            print("Mi doverman Anita su pelo es sepia")
        elif col == "lila":
            print("Siempre me han gustado los arreglos florales con lilas")
        elif col=="naranja":
            print("mi fruta favvvvvvvvvv es naranja")
        elif col == "beibi blue":
            print("dicen que el cielo es beibi blue porque diosito es niño jejejeje")
        elif col == "hueso":
            print("el esqueleto humano tienen 220 huesos")        