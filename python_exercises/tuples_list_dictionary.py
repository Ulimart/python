#fruit_tuple = ("apple", "banana", "strawberry", "orange")
#print(fruit_tuple.index("strawberry"))
#print(fruit_tuple.index("orange"))
#print((fruit_tuple[0]))
#print(sorted(fruit_tuple))
#del fruit_tuple[1]  ###  CON ESTE EJEMPLO PODEMOS NOTAR QUE CON TUPLE NO SE PUEDEN ALTERAR LA DATA, EN ESTE CASO ES ELIMINAR ALGUN ELEMENTO
#print(fruit_tuple)

#name_list = ["Juancho", "La Kimberly", "El Brayan", "Iker"]
#name_list = ["Juancho", "La Kimberly", "El Brayan", "Iker"]
#name_list.append(input("Add a name: "))
#del name_list[1]
#print(sorted(name_list))
#name_list.sort()
#print(name_list)

#colores = {1: "red", 2:"blue", 3:"green"}
#print(colores)
#colores[2] = "yellow"
#print(colores)

#x_list = [154,634,892,345,341,43]
#print(len(x_list))
#print(x_list[1:4]) # el 4 representa la posicion donde se detendrá el contador y el 1 es donde empieza, recordando que el primer numero es 0
#for i in x_list:
#    print(i)
#num = int(input("enter a number: "))
#if num in x_list:
#    print(num, "is in the list")
#else:
#    print("Not in the list")
#x_list.insert(2,420) ### representa la posición de la lista, 0,1,2,3... etc
#x_list.remove(892)
#x_list.append(993)
#print(x_list)

#country_tuple= ("Greece", "Mexico", "France", "Germany", "Turkey")
#print(country_tuple)
#print() #### Esto sería un espacio entre la linea de arriba y la siguiente, para que se vea más estético el display
#name_country = input("Enter one of the countries that have been shown u: ")
#print(country_tuple.index(name_country))
#print()
#number_country = int(input("Enter a number between 0-4 and i will display the country in that position: "))
#print("Your choose was the country: ", country_tuple[number_country])

#sports_list =  ["natation", "Aerial hoop"]
#print(sports_list)
#sports_list.append(input("Tell me your favorite sport: "))
#sports_list.sort()
#print(sports_list)

#school_subjects = ["art", "math", "music", "geography", "spanish", "french"]
#print(school_subjects)
#no_subjects= input("Tell me which is the subject u hate? and i will delete it ")
#school_subjects.remove(no_subjects)
#print(school_subjects)

###DICCIONARIO
#menu = {} ## se agrega una variable vacia para que se comience a llenar 
#print("Dime tus 4 comidas favoritas ")
#fav_food_01 = str(input("Escribe la primera: "))
#fav_food_01 = fav_food_01.capitalize()
#menu[1] = fav_food_01   ### para llenarla de agrega el numero que ocupara dicha opcion pero entre [ ] porque así formamos un diccionario
#fav_food_02 = str(input("Escribe la segunda: "))
#fav_food_02 = fav_food_02.capitalize()
#menu[2] = fav_food_02
#fav_food_03 = str(input("Escribe la tercera: "))
#fav_food_03 = fav_food_03.capitalize()
#menu[3] = fav_food_03
#fav_food_04 = str(input("La ultima: "))
#fav_food_04 = fav_food_04.capitalize()
#menu[4] = fav_food_04
#print(menu)
#no_laic = int(input("Del menú que te presenté antes, dime una que debería eliminar, del 1-4: "))
#del menu[no_laic]
#print(sorted (menu.values()))

#colores_list = ["rojo", "amarillo", "lila", "azul", "rosa", "menta", "naranja", "negro", "blanco", "dorado"]
#num_01 = int(input("Dime un numero del 0-4: "))
#num_02 = int(input("Escribe un numero entre el 5-9: "))
#print(colores_list[num_01:num_02]) 

#num_list = [892, 457, 321, 306]
#for i in num_list:
#    print(i)
#ask_num = int(input("Escribe un numero de 3 digitos y veamos si pensamos en el mismo: "))
#if ask_num in num_list:
#    print(ask_num, "está en la lista",num_list.index(ask_num)) ### INDEX ayuda a encontrar la posicion en la lista del numero/palabra que eligimos
#else:
#    print("Neeeeeeeeeeel, no la armas")   


#invi_01 = input("Dime el nombre del primer invitado: ")
#invi_02 = input("Dame el nombre del segundo invitado: ")
#invi_03 = input("Escribe el nombre del 3er invitado: ")
#invitados_list = [invi_01, invi_02, invi_03]
#ask = str(input("Quieres invitar a alguien más? Si (s) o no (n)?? "))
#while ask == "s":
#    invi_new = invitados_list.append(input("Dame el nombre del siguiente invitado: "))  ##DUDA: por qué la forma como yo agregué mis nombres estaba mal?
##    invitados_list = invitados_list.append(invi_new)
#    ask = input("Quieres invitar a alguien más? Si (s) o no (n)?? ")
#print("Has invitado", len(invitados_list), "personas, creo que va a salir cara la fiesta jajaajjaja")

#invi_01 = input("Dime el nombre del primer invitado: ")
#invi_02 = input("Dame el nombre del segundo invitado: ")
#invi_03 = input("Escribe el nombre del 3er invitado: ")
#invitados_list = [invi_01, invi_02, invi_03]
#ask = str(input("Quieres invitar a alguien más? Si (s) o no (n)?? "))
#while ask == "s":
#    invi_new = invitados_list.append(input("Dame el nombre del siguiente invitado: "))  
#    ask = input("Quieres invitar a alguien más? Si (s) o no (n)?? ")
#print("Has invitado a", invitados_list)
#preg = invitados_list.index(input("Dime el nombre de uno de tus invitados: "))
#print("El nombre que diste es el numero",preg,"en la lista")
#duda=input("Estas segurx que asista a la fiesta? si (s) o no (no)?? ")
#if duda == "n":
#    del invitados_list[preg]
#    print("entonces tu lista de invitados quedará así:",invitados_list)
#else:
#    print("Perfecto, espero la pases super bien y comas mucho pastel")
### en la respuesta el libro viene así:
#preg = input("Dime el nombre de uno de tus invitados: ")
#print("El nombre que diste es el numero",invitados_list.index(preg),"en la lista")
#duda=input("Estas segurx que asista a la fiesta? si (s) o no (no)?? ")
#if duda == "n":
#    invitados_list.remove(preg)
#    print("entonces tu lista de invitados quedará así:",invitados_list)

#tv_list = ["bitelyuz", "pagüer ranyers", "seilor mun", "dinosaurios"]
#for i in tv_list:
#    print(i)
#ask = input("Si quieres agregar otro programa de tv, escribelo: ")
##print(type(ask))
#posic = int(input("En que lugar de la lista te gustaría que estuviera, 0-3: "))
##print(type(posic))
#tv_list.insert(posic,ask)
#for i in tv_list:
#    print(i)
### por qué no sirvió mi magnífica idea de poner:
#tv_list = tv_list.insert(posic,ask)
#print(tv_list)

nums = []
cont = 0
while cont < 3:
    ask = (input("Dime un numero: "))
    nums.append(ask)
    print(nums)
    cont = cont + 1
preg = input("Quieres que guardemos el ultimo numero??? si (s) o no (n)?? ")
if preg == "n":
    nums.remove(ask)   #### ¡¡¡duda!!!
    print(nums)
else: 
    print("puuuuuuuuuuuuuuuuuuurfect")
  