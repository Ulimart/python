"""
CSV ==> Comma Separated Values

w => Creates a new file and writes to that file. If the file already
exists, a newfile will be created, overwriting the existing file.

x => Creates a new file and writes to that file. If the file already
exists, the program will crash rather than overwrite it.

r => Opens for reading only and will not allow you to make changes.

a => Opens for writing, appending to the end of the file.

"""

import csv  ### Library of commands

#file = open ("stars.csv", "w")
#newRecord = "Brian,73,Taurus\n"
#file.write(str(newRecord))
#file.close()

#file = open("stars.csv","a")
#name = input("Enter name: ")
#age = input("Enter age: ")
#star = input("Enter star sign: ")
#newRecord2 = name + "," + age + "," + star + "\n"
#file.write(str(newRecord2))
#file.close()

#file = open("stars.csv", "r")
#for row in file:
#    print(row)

#file = open("stars.csv", "r")
#reader = csv.reader(file)
#rows = list(reader)
#print(rows[1])

#file = open("stars.csv", "r")
#search = input("Enter the data you are searching for: ")
#reader = csv.reader(file)  ### AQUI SOLO LEE EL ARCHIVO DEVUELVE ALGO QUE TENGA RELACION CON LO QUE ESCRIBISTE
#for row in file:
#    if search in str(row):
#        print(row)

#file = list(csv.reader(open("stars.csv")))
#tmp = []
#for row in file:
#    tmp.append(row)

#file = open("niustars.csv", "w")
#x = 0
#for i in tmp:
#    newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
#    file.write(newRec)
#    x  = x + 1
#file.close()

"""
111.
Create a .csv file that will store the following data. 
Call it “Books.csv”.
"""
#file = open("Books.csv","w")
#nrec = "To Kill a Mockingbird,Harper Lee,1960\n"
#file.write(str(nrec))
#nrec = "A Brief History of Time,Stephen Hawking,1988\n"
#file.write(str(nrec))
#nrec = "The Great Gatsby,F. Scott Fitzgerald,1922\n"
#file.write(str(nrec))
#nrec = "The Man Who Mistook his Wife for a hat,Oliver Sacks,1985\n"
#file.write(str(nrec))
#nrec = "Pride and Prejudice,Jane Austen,1813\n"
#file.write(str(nrec))
#file.close()

"""
112.
Using the Books.csv file from program 111, ask the user to enter
another record and add it to the end of the file.
Display each row of the .csv file on a separate line.
"""
#file = open("Books.csv","a")
#titulo = input("Escribe el titulo del libro para agregarlo: ")
#autor = input("Ahora el autor del libro: ")
#año = input("El año en que fue escrito: ")
#nrec = titulo + "," + autor + "," + año + "\n"
#file.write(str(nrec))
#file.close()

"""
113. 
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. 
After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
"""

#preg = int(input("¿Cuántos libros quieres agregar?: "))
#file = open("Books.csv","a")
#for i in range(0,preg):
#    titulo = input("Escribe el titulo del libro ara agregarlo: ")
#    autor = input("Ahora el autor del libro: ")
#    año = input("El año en que fue escrito: ")
#    nrec = titulo + "," + autor + "," + año + "\n"
#    file.write(str(nrec))
#file.close()

#preg2 = input("Dime un autor que quieras que busque: ")
#file = open("Books.csv","r")
#chequeo = "hola" #### PREGUNTA
#for i in file:
#    if preg2 in str(i):
#        print(i)
#        chequeo = "adios"
    
#if chequeo == "hola":
#    print("Ese autor no se encuentra en la lista :/")
#file.close()

"""
114.
Using the Books.csv file, ask the user to enter a starting 
year and an end year. 
Display all books released between those two years.
"""
#num1 = int(input("Dame una fecha inicial: "))
#num2 = int(input("Dame una fecha final: "))

#file =list(csv.reader(open("Books.csv")))
#tmp = []
#for i in file:
#    tmp.append(i)
#x = 0
#for j in tmp:
#    if int(tmp[x][2]) >= num1 and int(tmp[x][2]) <= num2:
#        print(tmp[x])
#    x = x + 1
#print()

"""
115.
Using the Books.csv file, display the data in the file along 
with the row number of each.
"""
#file = open("Books.csv","r")
#x = 1
#for i in file:
#    ver = "Fila: " + str(x) + ".- " + i
#    print(ver)
#    x = x + 1

"""
116.
Import the data from the Books.csv file into a list. Display the
list to the user. 
Ask them to select which row from the list they want to delete 
and remove it from the list. 
Ask the user which data they want to change and allow them to 
change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
"""

#file = list(csv.reader(open("Books.csv")))
#tmp = []
#for i in file:
#    tmp.append(i)

#x = 0
#for j in tmp:
#    ver = x,tmp[x]
#    print(ver)
#    x = x + 1
#elim = int(input("Cuál de las filas quieres eliminar??: "))
#del tmp[elim]

#x = 0
#for j in tmp:
#    ver = x,tmp[x]  #### DE LA LISTA VA A IMPRIMIR LINEA A LINEA DE TMP
#    print(ver)
#    x = x + 1
#camb = int(input("Cuál de las filas quieres modificar??: "))
#x = 0
#for k in tmp[camb]:  ### AQUI ELEGIMOS UNA LINEA Y ESTA ES LA QUE VA A TOMAR EN EL FOR
#    ver = x,tmp[camb][x] ## DESPUES VA A DISECCIONARLA, CADA COLUMNA DE LA FILA QUE ELEGIMOS CAMBIAR
#    print(ver) ## LO CUAL VA A IMPRIMIR
#    x = x + 1
#camb2 = int(input("Qué parte de la tabla quieres cambiar?: ")) ## ELEGIMOS LA COLUMNA A CAMBIAR
#nuevo = input("Escribe lo que quieres cambiar: ")  ## QUE VAMOS A CAMBIAR
###print(tmp[camb][camb2])
#tmp[camb][camb2] = nuevo ## DE LA FILA QUE QUEREMOS CAMBIAR (tmp[camb]) Y LA COMLUMNA ELEGIDA ([camb2]) SE VA A RELLENAR CON "nuevo"
#print(tmp[camb]) # SE IMPRIME EL CAMBIO REALIZADO

#file = open("Books.csv","w")
#x = 0
#for m in tmp:
#    cambs = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
#    file.write(cambs)
#    x = x + 1
#file.close()

"""
117.
Create a simple maths quiz that will ask the user for their name and 
then generate two random questions. 
Store their name, the questions they were asked, their answers and 
their final score in a .csv file. 
Whenever the program is run it should add to the .csv file and not 
overwrite anything.
"""

import random

calif = 0
nombre = input("Escribe tu nombre: ")
num1 = random.randint(21,100)
num2 = random.randint(21,100)
preg1 = str(num1) + " x " + str(num2) + " = "
resp1 = int(input(preg1))
ope1 = num1 * num2
if resp1 == ope1:
    calif = calif + 3

num3 = random.randint(3,50)
num4 = random.randint(2,51)
preg2 = str(num4) + " - " + str(num3) + " = "
#print("tu respuesta debes de redondearla a dos decimales")
resp2 = float(input(preg2))
ope2 = num4 - num3
round(ope2,2)
if resp2 == ope2:
    calif = calif + 3

print("Tu calificación fue: ", calif)

file = open("calificaciones.csv","a")
alumno = nombre + "," + preg1 + "," + str(resp1) + "," + preg2 + "," + str(resp2) + "," + str(calif) + "\n"
file.write(str(alumno))
file.close()