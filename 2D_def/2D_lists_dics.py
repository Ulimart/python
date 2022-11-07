"""
En este caso se va a trabajar con bidimensional listas, que visualmente son 
tablas, donde pones nombres numeros.
Ejemplo:
Una tabla de calificaciones, la primera columna es para los nombres de los
alumnos, la segunda podría ser la calif de la primera tarea, la tercera
columna para la 2da tarea, etc etc
Por lo que entiendo solo es para listas, que usa corchetes, y diccionarios
que usan llaves. Pero para abrir el 2D se debe de empezar con corchetes.
Me recuerda a las mnatrices de m x n
"""

#simple_array = [[2,5,8],[3,7,4],[1,6,9]]
#print(simple_array)
#print(simple_array[1]) ### cuando se pone entre corchetes un numero te arroja la fila, recordamos que 0 ese el primer numero
#print(simple_array[1][2]) ### aqui devuelve el numero que se encuentra en la fila 1 y en la columna 2. Es una interseccion

#### para cambiar numeros dentro de la matriz, lo que puedes hacer es lo siguiente:
#simple_array[2][1]=5 ### se cambio el 6 => 5
#print(simple_array)

### para agregar valores:
#simple_array[1].append(3)
### en este caso se agrega en la fila 1, irá hasta el final, el numero 3
#print(simple_array)

### en este caso A y B son las filas y (x,y,z) son las columnas
#data_set = {"A":{"x":54, "y":82, "z":91}, "B":{"x":75, "y":29, "z":80}}
#print(data_set)
#print(data_set["A"])
#print(data_set["B"]["y"]) ### Devuelve el numero donde se hace hace la interseccion
#data_set["B"]["y"] = 53 ### se cambia el numero 29 => 53
#print(data_set["B"])

### Muestra los datos en la columna "y" en manera de espaciada
#for i in data_set:
#    print(data_set[i]["y"])


#### TENGO DUDAS DE ESO
###Adds another row of data to a 2D dictionary. In this case, name would be 
#### the row index and Maths and English would be the column indexes.
#grades[name] = {"Maths":mscore, "English":escore} 
### Displays only the name and the English grade for each student.
#for name in grades:
#    print((name),grades[name]["English"])
### Removes a selected item.
#del list[getRid]

"""
Create the following using a simple 2D list using the standard Python 
indexing:
"""
#tabla = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

"""
Using the 2D list from the last program, ask the user to select a row and a 
column and display that value.
"""
#row = int(input("Escribe un numero para buscar la fila, 0-3: "))
#col = int(input("Escribe un numero para buscar la columna, 0-2: "))
#print(tabla[row][col])

"""
Using the 2D list from program tabla, ask the user which row they would like 
displayed and display just that row. Ask them to enter a new value and
add it to the end of the row and display the row again.
"""
#row = int(input("escribe un numero del 0-3, ese será la fila que elijas: "))
#row_num = int(input("dame un numero para agregarlo a esa fila: "))
#tabla[row].append(row_num)
#print(tabla)

"""
100. Create the following using a 2D dictionary showing the sales each person has
made in the different geographical regions:
"""
#tabla = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
#print(tabla)

"""
Using program 100, ask the user for a name and a region. Display the relevant
data. Ask the user for the name and region of data they want to change and 
allow them to make the alteration to the sales figure. Display the sales for
all regions for the name they choose.
"""
#row = input("De la lista que te mostré anteriormente, que fila te interesa, recuerda que los nombres son las filas: ")
#col = input("Ahora escribe cual de los puntos cardinales quieres: ")
#print(tabla[row][col])
#nuevo = int(input("Escribe el numero que reemplace la interseccion de tu eleccion: "))
#tabla[row][col] = nuevo
#print(tabla[row])

"""
102. Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
"""
####Para este caso será en tipo diccionario, o sea con {}

tabla = { }
for i in range(4):
    nombre = input("Escribe un nombre: ")
    edad = int(input("Escribe la edad de esa persona: "))
    pie = int(input("Ahora la talla de su pie: "))
    tabla[nombre] = {"Edad":edad, "Talla":pie}
print(tabla)

#preg = input("Dime el nombre de las personas que están dentro de la tabla: ")
#print(tabla[preg])

"""
Adapt program 102 to display the names and ages of all the 
people in the list but do not show their shoe size.
"""
#for nombre in tabla:
#    print((nombre),tabla[nombre]["Edad"])

"""
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.
"""
elim = input("Escribe que persona de la lista quieres quitar: ")
del tabla[elim]

for nombre in tabla:
    print((nombre),tabla[nombre]["Edad"],tabla[nombre]["Talla"])
