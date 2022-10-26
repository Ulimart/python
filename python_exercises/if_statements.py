#num1= 45
#if num1 > 10:
#    print("mayor a 10")
#elif num1 == 10:
#    print("son igualesssss")
#else:
#    print("pues que es menor a 10, no hay de otra")

#num=4
#if num > 10:
#    print("mayor a 10")
#else:
#    print("pues que es menor a 10, no hay de otra")

#num=18
#if num >= 10:
#    if num <= 20:
#        print("esta entre 10 y 20")
#    else:
#        print("mmmmmm... creo que está arriba de 20")
#else:
#    print("abajo de 10")

#texto="Carolicious"
#print(str.lower(texto))

#num= int(input("echale un numero entre 10 y 20: "))
#if num >= 10 and num <= 20:
#    print("esoooooo")
#else:
#    print("te pedí un rango, vuelve a decirme otro numero")

#num= int(input("dame un numero PAR entre 1 y 5: "))
#if num == 2 or num == 4:
#    print("vayaaaaaaaaaaa, entendiste bien")
#else:
#    print("neta??? aprende a leer mejor y vuelve a intentarlo")

#num1= int(input("dame un numero "))
#num2= int(input("dame otro numero "))
#if num1 > num2:
#    print("entonces si los acomodamos debería ir primero ", num1, "y después ", num2)
#else:
#    print("bueno, va a ir primero ", num2, "y después ", num1)

#num= int(input("Dame un numero MENOR a 20 "))
#if num > 20:
#    print("aaaayyyy, te equivocaste, vuelve a leer y dame el numero correcto")
#else:
#    print("puuuuuuuuuuuuuuuuuurfect, continuemos con más juegos")

#num=int(input("Dame un numero entre 10 y 20, puedes incluir el 20: "))
#if num > 10 and num <= 20:
#    print("¡Bien hecho!")
#else:
#    print("no fue correcta la respuesta, vuelve a empezar")

#var=input("¿Qué color te gusta? ")
#if var == "rojo" or var == "ROJO" or var == "Rojo":
#    print("Wooooowwww, a mi también me gusta ese color")
#else:
#    print("No me gusta el", var, ", prefiero el rojo")

#resp=input("Oye, ¿está lloviendo? ")
#resp=str.lower(resp)
#if resp == "si":
#    resp2=input("¿hay demasiado viento?")
#    resp2=str.lower(resp2)
#    if resp2 == "si":
#        print("entonces no lleves sombrilla, se te va a perder")
#    else:
#        print("llevate esta sombrilla")
#else:
#    print("Disfruta el día que está bonito")
        
#resp=int(input("¿Que edad tienes, compiss? "))
#if resp >= 18:
#    print("ya eres mayor de edad, así que a votar!!!!")
#elif resp == 17:
#    print("Puedes aprender a manejar, así me llevas al supermercado")
#elif resp == 16:
#    print("Comprate un billete de loteria, a ver si así tienes suerte")
#else:
#    print("Mejor ve a pedir dulces en Jalogüin, jajajajajajaa")

#resp=int(input("A veeeer, dame un numero "))
#if resp < 10:
#    print("es un numero muy pequeño, dime otro")
#elif resp > 10 and resp < 20:
#    print("Puuuuuuuuuuuurfect!!!!")
#else:
#    print("numero incorrecto")


resp=int(input("elige un numero del 1 al 3 "))
if resp == 1:
    print("Draaaaaaaaaaacias")
elif resp == 2:
    print("Bien hecho")
elif resp == 3:
    print("Correctoooouuuuuuuuuuuuuuuu!!")
else:
    print("mmmmmm, puessss: numero incorrecto")