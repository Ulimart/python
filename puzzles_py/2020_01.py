file = open("puzzle_01.csv","r")

tmp = []
for u in file:
    tmp.append(u)

#print(type(tmp))

x = 0 
num = 2020
num_lst  = []
num_lst2 = []
#print(type(num))
#print(num)
for j in tmp:
    num2 = int(tmp[x])
    num1 = num - num2
    num_lst.append(num1)
    num_lst2.append(num2) 
#    print(num_lst[x])
    x = x + 1

from array import *

resp = array('i',[])
for k in num_lst2:
#    print(k)
#    print(type(k))
    for l in num_lst:
##        print(l)
#        print(type(l))
        if k == l:
#            print("jelou")
            print(l)
            resp.append(l)

#print(resp)
print("la suma de los numeros es: ", sum(resp))
a = resp[0]
b = resp[1]
c = a * b
print("La multiplicación entre ellos es: ", c)

file.close()
