### STRING: technical name for a group of characters that you do not need to perform calculations with. Example: “Hello”, "45c"

#msg = "CARO"
#msg = "caro"
#msg = "Caro"
#if msg.isupper():
#    print("Mayusculaaaaaaaaaaaaaaaaaa")
#else:
#    print("Esto qué rayos es??? Ascaaaaaa!!!")

#if msg.islower():
#    print("Minusculaaaaaaaaaaaaaaaaaa")
#else:
#    print("Esto qué rayos es??? Ascaaaaaa!!!")

#for letter in msg:
#    print(letter,end = "+") # sepuede usar otros simbolos :)

#nombre = str(input("Podrías escribir tu nombre: "))
#print("la longitud de tu nombre es:",len(nombre))
#apell = str(input("Ahora escribe tu apellido: "))
#print("la longitud de tu apellido es:",len(apell))
#completo = nombre + " " + apell
#print(completo)
#print("la longitud de tu nombre completo es:", len(completo))

#materia = input("Cuál es tu materia favvvvvvvvvvvvv??? ")
#for letter in materia:
#    print(letter,end="<")

#print ("No sé de poemas, pero te escribiré una frase simpática: ")
#poema = "Y la que soporteeeee, panzonas"
#print(poema)
#print(len(poema))
#inicio = int(input("Escribe un numero: "))
#fin = int(input("Escribe otro numerazooooooooo: "))
#print("De los numeros que me diste se encuentran los siguientes caracteres de mi aiiiconicccc freiiiissssss:", poema[inicio:fin])

#palabra = input("Escribe una palabra en mayuscula, beibiii: ")
#mayus = False
#while mayus == False:
#    if palabra.isupper():
#        print("Esooooooooooooooooooooooooooooooo!!!!")
#        mayus = True
#    else:
#        palabra = input("Vuelve a intentarlo, escribe una palabra en mayusculassss: ")

#codig = input("Escribe tu codigo postal: ")
#postal = codig[0:2]
#print(postal.upper())

#nombre = input("Escribe tu nombre: ")
#nombre = nombre.lower()
#conteo = 0
#for i in nombre:
#    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#        conteo = conteo + 1
#print("tu nombre tiene",conteo,"vocales")

#pswd = input("Escribe la nueva contraseña que quieres para tu insta: ")
#pswd2 = input("Vuelve a escribir la contraseña: ")
#if pswd == pswd2:
#    print("Gracias ;)")
#elif pswd.isupper() != pswd2.isupper():
#    print("No tienen el mismo el mismo formato")
#elif pswd.islower() != pswd2.islower():
#    print("No tienen el mismo el mismo formato")
#else: 
#    print("Contraseña incorrecta")

#palabra = input("Escribe una palabra: ")
#palabra_alreves = palabra[:: -1]
#print(palabra_alreves)
#for i in palabra_alreves:
#    print(i)

### En el libro viene de esta manera:
palabra = input("Escribe una palabra: ")
palab2 = len(palabra)
num = 1
for i in palabra:
    lugar = palab2 - num
    palab3 = palabra[lugar]
    print(palab3)
    num = num + 1