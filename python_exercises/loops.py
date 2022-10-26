#for i in range(1,10):
#    print(i)

#for i in range(1,10,2):  ### el tercer numero es que el que se agrega al numero, o se, 1+2, 3+2, etc.
#    print(i)

#for i in range(10,1,-3):  ### en este caso se le resta el 3er numero, pero debemos agregar el ultimo numero del rango y después el primero
#    print(i)

#for i in "carolina":   ### muestra cada letra de la palabra que se agrega en el loop
#    print(i)

#nom=input("Escribe tu nombre y aparecerá 3 veces ")
#for r in range (0,3):
#    print(nom)

#nom=input("Escribe tu nombre y aparecerá 3 veces ")
#rep=int(input("Cuántas veces quieres que se repita tu nombre? "))
#for i in range(0,rep):
#    print(nom)

#nom=input("Escribe tu nombre ")
#for i in nom:
#    print(i)

#nom=input("Escribe tu nombre ")
#rep=int(input("Dame un numero "))
#for i in range(0,rep):  ### numero de repeticiones
#    for r in nom:       ### que va a repetir
#        print(r)

#var=int(input("escribe un numero entre 1 y 12 "))
#for i in range(1,13):
#    num= i * var
#    print(i,"x",var, "=",num)

#var=int(input("Escribe un numero antes del 50: "))
#for i in range(var,51):
#    print(i)

#var=int(input("Escribe un numero antes del 50: "))
#for i in range(50,var-1,-1):   #### Para este caso a var se le resta 1, si elijo el numero 38, quedaria 37, entonces va del 50 al 37 y sí toma el 38
#    print(i)

#nom=input("holiii compita, hagamos magia, dame tu nombre ")
#num=int(input("ahora un numero: "))
#if num < 10:
#    for i in range(0,num):
#        print(nom)
#else:
#    for i in range(0,3):
#        print("Numero muy grande")

#total=0
#for i in range(0,5):
#    num=int(input("Dame un numero: "))
#    var=input("quieres incluir ese numero a la magia? si o no: ")
#    if var=="si":
#        total=total + num
#print(total)

#preg=input("Vamos a contar, quieres que el conteo empiece de arriba hacia abajo o viceversa? up o down? ")
#if preg == "up":
#    num= int(input("Dame el numero hasta donde quieres que termine el conteo: "))
#    for i in range(1,num+1):
#        print(i)
#elif preg == "down":
#    num= int(input("Dame un numero abajo de 20: "))
#    for i in range(20,num-1,-1):
#        print(i)
#else:
#    print("no te entiendo, byeeeeeeeeeeeeeee!!!")

#invitados=int(input("Cuántas personas vas a invitar a la fiesta?? "))
#if invitados < 10:
#    for i in range(0,invitados):
#        nom=input("Dime el nombre, uno por uno: ")
#        print(nom, "incluido en la lista")
#else:
#    print("ay nooooo, son muchos, se cancela la fiesta")

######################## WHILEEEEEEEEEEEE LOOPSSSSSSSSSSSSS ###################################

#resp="si"
#while resp == "si":
#    print ("hola friends")
#    resp = input("Quieres que se vuelva a repetir?? ")

#total = 0
#while total < 100:
#    num=int(input("Escribe un numero: "))
#    total = total + num
#print("El total es", total)

#total=0
#while total <= 50:
#    num=int(input("Escribe un numero: "))
#    total = total + num
#print("el total es",total)

#num=0
#while num < 5:
#    num=int(input("Escribe un numero: "))
#print("El ultimo numero que escribiste fue:",num)

#num1=int(input("Dame un numero: "))
#total=num1
#resp="si"
#while resp== "si":
#    num2=int(input("Dime otro: "))
#    total= total + num2
#    resp=input("¿Quieres sumar otro numero? si o no? ")
#print(total)

#resp="si"
#invit=0
#while resp == "si":
#    nam=input("A quién vas a invitar a la fiesta? ")
#    print(nam,"se va a contar como parte de los invitados.")
#    invit=invit + 1
#    resp= input("invitaras a alguien más?, si o no? ")
#print("Llevas",invit,"invitados agregados a la lista")

##ESTA MAL ESTE LOOP
#compnum=50
#cont=0
#while compnum == 50:
#    compnum=int(input("Adivina el numero en el que estoy pensado, escribelo: "))
#    cont=cont + 1
#    if compnum < 50:
#        print("No le atinaste, esta más abajo, vuelvelo a intentar ")
#    elif compnum > 50:
#        print("no le atinaste, el numero esta más arriba del que estoy pensando, vuelvelo a intentar ")
#    else:
#        print("le atinaste")
#print ("Le atinaste a la respuesta en el intento numero: ",cont)

##Siguiente intento

compnum=50
cont=1
preg=int(input("Adivina el numero que estoy pensando: "))
while compnum != preg:
    cont=cont + 1
    if compnum > preg:
        print("No es el mismo numero, es mucho más pequeño ")
    else:
        print("No es el mismo numero, es mucho más grande ")
    preg=int(input("Otra oportunidad, dame un numero: "))
print("Lo lograste al intento numero:",cont)
    
#preg=int(input("dime un numero entre 10 y 20: "))
#while preg < 10 or preg > 20:
#    if preg < 10:
#        print("numero pequeño")
#    else:
#        print("numero muy grande")
#    preg=int(input("vuelve a intentarlo: "))
#print("logrado")


### DUDA PREGUNTAR  A ULI ####
#num=10
#while num >0:
#    print("There are",num,"green bottles hanging on the wall,")
#    print(num,"green bottles hanging on the wall, ")
#    print("and if 1 green bottle should accidentally fall.")
#    num=num - 1
#    preg=int(input("How many green bottles will be hanging on the wall? "))
#    if preg == num:
#        print("There will be",num,"green bottles hanging on the wall.")
#    else:
#        while preg != num:
#            preg=int(input("No, try again: "))
#print("There are no more green bottles haging on the wall")




