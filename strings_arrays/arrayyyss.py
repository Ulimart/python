#### Los arrays son usados solamente para guardar numeros, se deben de definir el tipo de data que va a contener el array.
#### LOS TIPOS DE ARRAY: 
###   i => integer
###   f => float-point
###   l => long
###   d => double

from array import *
from audioop import lin2alaw   ### para trabajar con los arrays se necesita la libreria array

#nums = array('i', [45, 324, 654, 45, 264])
#print(nums)

#for x in nums:
#    print(x)

#valor = int(input("Escribe un numero frienddddd: "))
#nums.append(valor)
#print(nums)

#nums.reverse()
#nums = sorted(nums)  ## la acomoda de manera ascendente
#nums.pop()  ## Elimina el ultimo numero de la fila
#print(nums)

#newArray = array('i', [])
#mas = int(input("Cuantos numeros agregamos al array??: "))
#for y in range(0,mas):
#    valor = int(input("Escribe el numero que agregaremos: "))
#    newArray.append(valor)
#    nums.extend(newArray)  ### Aqui agregamos al array nums el array de este ejercicio
#print(nums)

#getRid =int(input("Dime un numero del array que tenemos: "))
#nums.remove(getRid) ### Elimina el numero que haga match con el que escribiste
#print(nums)
#print(nums.count(45)) ## Te da el numero de veces que aparece el item entre parentesis

#num = array('i', [])
#for y in range(0,5):
#    valor = int(input("Escribe el numero que agregaremos: "))
#    num.append(valor)
#num = sorted(num)
#num.reverse()
#print(num)

#import random
#num = array('i',[])
#for x in range(0,5):
#    valor = random.randint(1,30)
#    num.append(valor)

#for x in num:
#    print(x)

"""Ask the user to enter numbers. If they enter a number between 10 and 20, 
save it in the array, otherwise display the message “Outside the range”. Once five numbers have been successfully added,
display the message “Thank you” and display the array with each item shown on a separate line."""
#num = array('i',[])
#valor = int(input("Escribe un numero: "))
#count = 0
#preg = False
#while preg == False:
#    if valor >= 10 and valor <= 20:
#        num.append(valor) 
#        count = count + 1
#        print("Gracias mijooooooo")
#        if count == 5:
#            preg = True
#    else:
#        print("Fuera del rango, vuelve a intentarlo")
#    valor = int(input("Escribe un numero: "))

#for x in num :
#    print(x)

"""Create an array which contains five numbers (two of which should be repeated).
Display the whole array to the user. Ask the user to enter one of the
numbers from the array and then display a message saying
how many times that number appears in the list"""
#lila = array('i',[21,3,45,21,88])
##print(lila)
#for i in lila:
#    print(i)
#num = int(input("Escribe un numero de los que viste anteriormente: "))
##print(type(num))
#print("El numero que elegiste aparece",lila.count(num),"veces en el arreglo")

"""Create two arrays (one containing three numbers that the user enters and one
containing a set of five random numbers). Join these two arrays together into one
large array. Sort this large array and display it so that each number appears
on a separate line."""

#import random
#lila = array('i',[])
#rose = array('i',[])

#for i in range(0,3):
#    valor = int(input("Escribe un numero: "))
#    lila.append(valor)
#print(lila)

#for x in range(0,5):
#    valor1 = random.randint(1,30)
#    rose.append(valor1)  
#print(rose)

#lila.extend(rose)
#lila = sorted(lila)
#for y in lila :
#    print(y)

"""Ask the user to enter five numbers. Sort them into order and present them
to the user. Ask them to select one of the numbers. Remove it from the original
array and save it in a new array."""

#rose = array('i',[])
#for i in range(0,3):
#    valor = int(input("Escribe un numero: "))
#    rose.append(valor)

#rose = sorted(rose)
#for x in rose:
#    print(x)

#preg = int(input("Elige un numero del arreglo: "))
#rose.remove(preg)
#print(rose)

"""Display an array of five numbers. Ask the user to select one of the numbers.
Once they have selected a number, display the position of that item in the
array. If they enter something that is not in the array, ask them to try
again until they select a relevant item."""

#lila = array('i',[100,5069,2,19,21])
#for x in lila:
#    print(x)

#rose = int(input("Elige uno de los numeros del arreglo: ")) 
#preg = True
#while preg == True:
#    if rose in lila:
#        print("El numero que elegiste se encuentra en la posicion",lila.index(rose),"del arreglo")
#        preg = False
#    else:
#        rose = int(input("No se encuentra en el arreglo. Quieres volver a intentarlo?? Escribe el numero: "))

"""Create an array of five numbers between 10 and 100 which each have two decimal
places. Ask the user to enter a whole number between 2 and 5. If they enter 
something outside of that range, display a suitable error message and ask them 
to try again until they enter a valid amount. Divide each of the numbers in the 
array by the number the user entered and display the answers shown to two decimal
places."""

import math

bril = array('f',[23.78,79.05,65.73,210.46,73.45])
preg = True 
while preg == True:
    num = int(input("Escribe un numero entre 2 y 5: "))
    if num > 2 and num < 5:
        num = num
        preg = False
    else:
        print("Mega Error, vuelvelo a intentar")

for i in range(5):
    div = bril[i]/num
    print(round(div,2))



