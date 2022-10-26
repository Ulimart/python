################################ STRINGS AND NUMBERS AS VARIABLES ################################

#pru = str("Hola amikessss")
#print(len(pru))
#print(pru.upper()) ### antes del punto se pone el nombre de la variable y entre los parentesis debe de ir vacio
#print(pru.lower())
#print(pru.title())
#print(pru.capitalize())

##nom = "Caro" 
##apel = "Montaño"
#nom = str("Caro")
#apel = str("Montaño")
#name = nom + apel  ### Esto es concatenar, no hay espacio entre lo que se "suma"
#print(name)

#print("Hola amikessss"[7:10]) ### Python comienza a contar desde el 0, en este caso el 0 es la H
#print("Hola amikessss"[0:4]) # el 4 es el espacio, porque cuenta espacios

#nom = input("Dame tu primer nombre: ")
#print(len(nom))

#nom = input("Dame tu nombre: ")
#apel = input("Dime tu apellido: ")
##nombre = nom + apel ### para que tenga espacio entre los dos strings se recomienda dar un espacio antes de la segunda variable
#nombre = nom + " " + apel ### otra mejor manera de tener un espacio es agregarlo
#print(nombre)
#print(len(nombre))

#nom = input("Nombre señor y en minusculas!! ")
#apel = input("Apellido y en minusculas!!! ")
#nombre = nom + " " + apel
#print(nombre.title())

#canc = input("Echate una frase perrona: ")
#len1 = len(canc)
#print("tu frase perrona tiene este numero de caracteres: ", len1)
#num1 = int(input("dime un numero del 0 al que aparecio anteriormente: "))
#num2 = int(input("dame otro, no tomes en cuenta el 0: "))
#print(canc[num1:num2])
###print(canc)

#var = input("dame una palabra ")
#print(var.upper())

#nom= input("Cuál es tu nombre? ")
##len1= int(len(nom))
##len1= (len(nom))
#if len(nom) < 5:
#    apel=input("¿Cuál es tu apellido? ")
#    nombre= nom + apel
#    print(nombre.upper())
#else:
#    print(nom.lower())

#pal = input("dame una palabra ")
#pal = pal.lower() ### se agregó esta linea aqui debido a que es la unica manera para cumplan el condicional
#pal1= pal[0]
#len1= len(pal)
#abra=pal[1:len1]
#if pal1 != "a" and pal1 != "e" and pal1 != "i" and pal1 != "o" and pal1 != "u":
#    compl= abra + pal1 + "ay"
#else:
#    compl=pal + "way"
#print(compl)


##############################  MATHS  #####################################

import math

#num=79.917392
#print(math.sqrt(num))
#print(round(num,2))
#print(num*math.pi)

#num= float(input("Ingresa un numero: "))
#print(num * 2)
#num1=num * 2
#print(round(num1,2))

#num=float(input("Dame un numero arriba de 500 "))
#num=math.sqrt(num)
#print(round(num,2))

#pi=math.pi
#print(round(pi,5))

#radio=int(input("Dime el radio de un circulo, porfitasssss ")) ###En este caso solo di un valor entero, si quiero añadir decimales uso float
#area= math.pi * (radio ** 2)
#print(area)
#alt=float(input("usando area anterior, dame la altura del cilindro para obtener el volumen "))
#vol=area * alt
#print(round(vol,3))

#print("dame dos numeros para hacer una division, sas? ")
#num1=int(input("primer numero: "))
#num2=int(input("segundo numero: "))
#div=num1//num2 ### doble / te entrega el cociente
#res=num1%num2 ### el % te entrega el residuo de una division
#print(num1,"dividido entre",num2,"da como cociente",div,"y el residuo es", res)

fig= int(input("1. Cuadrado \n2. Triangulo \nEscoge la figura que más te guste "))
if fig==1:
    ladocuad=int(input("Dame la medida de un lado del cuadrado para obtener el área: "))
    area= ladocuad**2
    print("El cadrado tiene un área de", area)
elif fig==2:
    basetrian=int(input("Por favor, dame el valor de la base del triangulo: "))
    alturatrian=int(input("Ahora, escribe la altura del triangulo: "))
    area=(basetrian * alturatrian)/2
    print("El área del triangulo es ", area)
else:
    print("Lo siento, esto es un error")



