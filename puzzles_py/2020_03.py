file = open("puzzle_02.csv","r")

lst = []
for u in file:
    lst.append(u)

x = 0
numin = []
numan = []
letra = []
for v in lst:
    m = lst[x][0] + lst[x][1]
    m = int(m)
    numin.append(m)
    p = lst[x][3] + lst[x][4]
    p = int(p)
    numan.append(p)
    r = lst[x][6]
    letra.append(r)
        #print(type(lst[x][0]))
    x = x + 1

file = open("puzzle_02_02.csv","r")

lst2 = []
for u in file:
    lst2.append(u)
x = 0
a = 0
for w in lst2:
    ult = len(lst2[x])
    ult = ult-1
    let = letra[x]
    rest = lst2[x][0:ult]
    num = rest.count(let)
#    print(num)
    mini = numin[x]
    maxi = numan[x]
    if num >= mini and num <= maxi:
        a = a + 1
        print("pues cayó el primer numero")
    x = x + 1

print("EL numero de configuraciones validas fueron: ", a)