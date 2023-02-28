file = open("puzzle_01.csv","r")

lst = []
for u in file:
    lst.append(u)

x = 0
#num = 2020
num_lst  = []
#num_lst2 = []
for v in lst:
    w = int(lst[x])
    num_lst.append(w)
#    num_lst2.append(num2) 
##    print(num_lst[x])
    x = x + 1
#print(type(num_lst))
#print(type(w))

from array import *

resp = array('i',[])
for i in num_lst:
    for j in num_lst:
        for k in num_lst:
            num = i + j + k
            if num == 2020:
#                print(i)
                resp.append(i)

resp = set(resp)
print(resp)
print("la suma de los numeros es: ", sum(resp))
resp = list(resp)
a = resp[0]
b = resp[1]
c = resp[2]
d = a * b * c
print("La multiplicación entre ellos es: ", d)

file.close()
