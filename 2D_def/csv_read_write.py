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

file = open ("stars.csv", "w")
newRecord = "Brian,73,Taurus\n"
file.write(str(newRecord))
file.close()

file = open("stars.csv","a")
name = input("Enter name: ")
age = input("Enter age: ")
star = input("Enter star sign: ")
newRecord2 = name + "," + age + "," + star + "\n"
file.write(str(newRecord2))
file.close()

file = open("stars.csv", "r")
for row in file:
    print(row)

file = open("stars.csv", "r")
reader = csv.reader(file)
rows = list(reader)
print(rows[1])

file = open("stars.csv", "r")
search = input("Enter the data you are searching for: ")
reader = csv.reader(file)  ### AQUI SOLO LEE EL ARCHIVO DEVUELVE ALGO QUE TENGA RELACION CON LO QUE ESCRIBISTE
for row in file:
    if search in str(row):
        print(row)

file = list(csv.reader(open("stars.csv")))
tmp = []
for row in file:
    tmp.append(row)

file = open("niustars.csv", "w")
x = 0
for i in tmp:
    newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
    file.write(newRec)
    x  = x + 1
file.close()



"""
Create a .csv file that will store the following data. 
Call it “Books.csv”.
"""
