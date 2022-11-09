"""
Subprograms are blocks of code which perform specific
tasks and can be called upon at any time in the program to
run that code.

Advantages

 You can write a block of code and it can be used and re-
used at different times during the program.

 It makes the program simpler to understand as the code
is grouped together into chunks.

def => hace referencia a la definicion de programas
A function is like a miniprogram within a program.
Por lo que se entiende es que def define una funcion
"""
#### Algo SENCI

#def hello():  ### Statement, va a definir 
#    print("howdy!!!!")
#    print("Amikooooooo")
#    print("hola a todos!!!!")

#hello()
#hello()
#hello()


#def hello(name):
#    print("Holiii, " + name)
#hello(" Eli")

"""
en el caso e def se tienen 5 terminos:
i. Definir
ii. Llamar
iii. Pasar
iv. argumento
v. parametro

En el codigo de acontinuacion, def esta DEFINIENDO a sayHello, LLAMA
al PARAMETRO name, la cual contiene el ARGUMENTO y por ultimo
PASA la info al codigo. 
"""

#def sayHello(name):  #### 1. define a sayHello 2.parametro => name
#    print("Holiii, " + name)
#sayHello("Querida")  ### Argumento => Querida


### Este subprograma va a preguntar el nombre y lo devuelve en la variable "user_name"
#def get_name():
#    user_name = input("Enter your name: ")
#    return user_name

### El subprograma va a desplegar el msj HELLO y el user_name
#def print_Msg(user_name):
#    print("Hello ", user_name)

### subprogram will get the user_name from the get_name() subprogram
###(using the variable user_name) as this was returned from the get_name() subprogram. It
##will then use that user_name variable in the print_Msg() subprogram.
#def main():
#    user_name = get_name()
#    print_Msg(user_name)

#main()

"""
IMPORTANT NOTE:
Python does not like surprises, so if you are going
to use a subprogram in a program, Python must have read the
“def subprogram_name()” line before so it knows where to
go to find it. If you try to refer to a subprogram before Python has
read about it, it panics and will crash. When calling a
subprogram, the subprogram must be written above the section
of code you use to call it. Python will read from the top down and run the first line it comes
across that has not been indented and does not start with the word def. In the program
above this would be main().
"""

#def get_data():
#    user_name = input("enter your name: ")
#    user_age = int(input("enter your age: "))
#    data_tuple = (user_name, user_age)
#    return data_tuple

#def message(user_name,user_age):
#    if user_age <= 10:
#        print("Hi", user_name)
#    else:
#        print("Hello", user_name)

#def main():
#    user_name,user_age = get_data()
#    message(user_name,user_age)


#main ()

"""
Define a subprogram that will ask the user to enter a number and 
save it as the variable “num”. Define another subprogram that 
will use “num” and count from 1 to that number.
"""
#def get_data():
#    num = int(input("Escribe un numero, arriba de 1: "))
#    return num

#def count(num):
#    i = 1
#    while i <= num:
#        print(i)
#        i = i + 1

#def main():
#    num = get_data()
#    count(num)

#main()

"""
119.
Define a subprogram that will ask the user to pick a low and a high
number, and then generate a random number between those two values
and store it in a variable called “comp_num”.
"""

#import random

#def num():
#    low_num = int(input("elige un numero: "))
#    high_num = int(input("elige un numero más grande que el anterior: "))
#    comp_num = random.randint(low_num,high_num)
#    return comp_num

"""
Define another subprogram that will give the instruction “I am
thinking of a number...” and then ask the user to guess the number
they are thinking of.
"""
#def adivina():
#    print("Estoy pensando en un numero")
#    dime = int(input("Adivina el numero en el que estoy pensando: "))
#    return dime

"""
Define a third subprogram that will check to see if the comp_num 
is the same as the user’s guess. If it is, it should display the
message “Correct, you win”, otherwise it should keep looping, 
telling the user if they are too low or too high and asking them
to guess again until they guess correctly.
"""

#def comparacion(comp_num,dime):
#    intento = True
#    while intento == True:
#        if comp_num == dime:
#            print("Esooooooooooooo!!! Adivinaste, haces magia!!!!")
#            intento = False
#        elif comp_num > dime:
#            adivina = int(input("Es un numero menor al que estoy pensando, vuelve a intentarlo: "))
#        else:
#            adivina = int(input("Es un numero mayor al que estoy pensando, vuelve a intentarlo: "))
    
#def main():
#    comp_num = num()
#    dime = adivina()
#    comparacion(comp_num,dime)

#main()

"""
120. Display a menu to the user.

If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.
"""
#import random

#def suma():
#    num1 = random.randint(5,20)
#    num2 = random.randint(5,20)
#    print("Voy a hacer la siguiente operación:",num1,"+",num2)
#    resp_usuario = int(input("Escribe la respuesta de la suma: "))
#    resp_oper = num1 + num2
#    resp = (resp_usuario, resp_oper)
#    return resp

"""
If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
"""

#def resta():
#    num3 = random.randint(25,50)
#    num4 = random.randint(1,25)
#    print("Voy a hacer la siguiente operación:",num3,"-",num4)
#    resp_usuario = int(input("Escribe la respuesta de la resta: "))
#    resp_oper = num3 - num4
#    resp = (resp_usuario, resp_oper)
#    return resp    
    
"""
Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.

If they do not select a relevant option on the first menu
you should display a suitable message.
"""

#def chequeo(resp_usuario, resp_oper):
#    if resp_usuario == resp_oper:
#        print("Pasaste el examen de matemáticas básicas")
#    else:
#        print("Debes volver a tus cursos de matemáticas básicas, la respuesta es:",resp_oper)

#def main():
#    print("1. Suma")
#    print("2. Resta")
#    selec = int(input("Escribe la opción que más te guste: "))
#    if selec == 1:
#        resp_usuario, resp_oper = suma()
#        chequeo(resp_usuario, resp_oper)
#    elif selec == 2:
#        resp_usuario, resp_oper = resta()
#        chequeo(resp_usuario, resp_oper)   
#    else:
#        print("Tu elección no es parte del menú")     

#main()

"""
121.
Create a program that will allow the user to easily manage a list
of names. You should display a menu that will allow them to add a 
name to the list, change a name in the list, delete a name from the
list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select 
an option that is not relevant, then it should display a suitable 
message. After they have made a selection to either add a name, 
change a name, delete a name or view all the names, they should see
the menu again without having to restart the program. The program
should be made as easy to use as possible.
"""

#nombres = []
#def agr_nombre():
#    nombre = input("Escribe un nombre para añadir a la lista: ")
#    nombres.append(nombre)
#    return nombres

#def cambiar_nombre():
#    num = 0
#    for i in nombres:
#        print(num,i)
#        num = num + 1
#    selec_nombre = int(input("Elije el numero del nombre que quieres cambiar: "))
#    nombre = input("Escribe el nuevo nombre: ")
#    nombres[selec_nombre] = nombre
#    return nombres

#def elim_nombre():
#    num = 0
#    for i in nombres: 
#        print(num,i)
#        num = num + 1
#        selec_nombre = int(input("Elije el numero del nombre que quieres eliminar: "))
#    del nombres[selec_nombre]
#    return nombres

#def ver_list():
#    for i in nombres:
#        print(i)
#    print()

#def principal():
#    repeticion = "y"
#    while repeticion == "y":
#        print("1. Agrega tu nombre faaaaaaaaaaav")
#        print("2. Cambiar el nombre que ya no quieres")
#        print("3. Elina el nombre que te parezca feo")
#        print("4. Ver la listerrima de nombres")
#        print("5. Yaaaa!!! Estaaaaaaaaap a las llamadas, ya no quiero ver nada!!")
#        elegir = int(input("Que numero del menú quieres: "))
#        if elegir == 1:
#            nombres = agr_nombre()
#        elif elegir == 2:
#            nombres = cambiar_nombre()
#        elif elegir == 3:
#            nombres = elim_nombre()
#        elif elegir == 4:
#            nombres = ver_list()
#        elif elegir == 5:
#            repeticion = "n"
#        else: 
#            print("Esa elección no existe en este menú, queridaaaaaaaaaaaaa")

##nombres = []
#principal()

"""
122. Create a menu

If the user selects 1, allow them to add to a file called Salaries.csv
which will store their name and salary. 
If they select 2 it should display all records in the Salaries.csv
file. 
If they select 3 it should stop the program. 
If they select an incorrect option they should see an error message. 
They should keep returning to the menu until they select option 3.
"""
import csv

def agr_file():
    file = open("Salaries.csv","a")
    nombre = input("Escribe un nombre: ")
    salario = int(input("Escribe el salario: "))
    algo = nombre + ", " + str(salario) + "\n"
    file.write(str(algo))
    file.close()

def ver_algo():
    file = open("Salaries.csv","r")
    for row in file: 
        print(row)
    file.close()

