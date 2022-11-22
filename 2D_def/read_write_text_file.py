"""
The easiest place to start learning about writing and reading from
an external file is with a text file.
When opening an external file you must specify how that file will be used within the
program. The options are below.

w => Write mode: used to create a new file. Any existing files
with the same name will be erased and a new one created in its 
place.

r => Read mode: used when an existing file is only being read and 
not being written to.

a => Append mode: used to add new data to the end of the file.

Text files are only used to write, read and append data.
By the very nature of how they work it is not easy to remove or 
alter individual elements of data once it is written to the file,
unless you want to overwrite the entire file or create a new file 
to store the new data. 
If you want to be able to alter the individual elements once the 
file has been created it is better to use a .csv file or an SQL 
database.
"""

### Aqui se van a crear un file llamado Countries. The \n forces a
### new line after each entry.

#file = open("Countries.txt","w")
#file.write("Italy\n")
#file.write("Germany\n")
#file.write("Spain\n")
#file.close()

### se supone que aqui abre el archivo pero no sé donde quedo!!!
#file = open("Countries.txt","r")
#print(file.read())
##print(file)

#file = open("Countries.txt","a")
#file.write = ("France\n")
### if we dont include the next line, the changes will not be 
### saved to the text file.
#file.close()

"""
            Write a new file called “Numbers.txt”. 
Add five numbers to the  document which are stored on the same 
line and only separated by  a comma. Once you have run the program, 
look in the location where your program is stored and you should 
see that the file has been created. 
The easiest way to view the contents of the new text file on a 
Windows system is to read it using Notepad.
"""

#file = open("Numbers.txt","w")
#file.write("21, ")
#file.write("88, ")
#file.write("3, ")
#file.write("87, ")
#file.write("22, ")
#file.close()

#file = open("Numbers.txt","r")
#print(file.read())
#file.close()

"""
            Create a new file called “Names.txt”. 
Add five names to the document, which are stored on separate lines.
Once you have run the program, look in the location where your 
program is stored and check that the file has been created 
properly.
"""

#file = open("Names.txt","w")
#file.write("Caro\n")
#file.write("Mati\n")
#file.write("Eli\n")
#file.write("Mamabi\n")
#file.write("Fer\n")
#file.close()

"""
Open the Names.txt file and display the data in Python.
"""

#file = open("Names.txt","r")
#print(file.read())
#file.close()

"""
Open the Names.txt file. Ask the user to input a new name. 
Add this to the end of the file and display the entire file.
"""

#file = open("Names.txt","a")
#nombre = str(input("Escribe el nombre que debemos agregar: "))
#file.write(nombre + "\n")
#file.close()

"""
            Display a menu to the user:
Ask the user to enter 1, 2 or 3. If they select anything other than
1, 2 or 3 it should display a suitable error message.

If they select 1, ask the user to enter a school subject and save 
it to a new file called “Subject.txt”. 
It should overwrite any existing file with a new file.

If they select 2, display the contents of the “Subject.txt” file.

If they select 3, ask the user to enter a new subject and save it 
to the file and then display the entire contents of the file.
Run the program several times to test the options.
"""

#print("1. Añadir una materia de la carrera universitaria que cursaste")
#print("2. Ver el contenido de tu documento")
#print("3. Agregar más contenido a tu documento")

#select = int(input("Elige el numero de las opciones que se mostraron anteriormente: "))

#if select == 1:
#    materia = input("Agrega la materia: ")
#    file = open("Subject.txt", "w")
#    file.write(materia + "\n")
#    file.close()
#elif select == 2:
#    file = open("Subject.txt", "r")
#    print(file.read())
#    file.close()
#elif select == 3:
#    file = open("Subject.txt","a")
#    new_materia = str(input("Escribe el otra materia que quieras agregar: "))
#    file.write(new_materia + "\n")
#    file.close()
#else:
#    print("Tu elección no está en el menú")

"""
Using the Names.txt file you created earlier, display the list of names 
in Python. Ask the user to type in one of the names and then save all 
the names except the one they entered into a new file called Names2.txt.
"""

file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
nombre = input("Escribe uno de los nombres que ya no quieras tener en tu lista: ")
nombre = nombre + "\n"
for x in file:
    if x != nombre:
#        print(file.read())
        file = open("Names2.txt","a")
        nuevo = x
#        print(nuevo)
        file.write(nuevo)
        file.close()
file.close()
