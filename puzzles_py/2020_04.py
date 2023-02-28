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
c = 0
for w in lst2:
    ult = len(lst2[x])
    ult = ult-1
    let = letra[x]
    print(let)
    rest = lst2[x][0:ult]

    num1 = numin[x]
    num1 = num1 - 1
    let1 = rest[num1]
    print(let1)

    num2 = numan[x]
    num2 = num2 - 1
    let2 = rest[num2]
    print(let2)

    if let == let1:
        a = 1
        print(a)
    elif let != let1:
        a = 2
        print(a)

    if let == let2:
        b = 1
        print(b)
    elif let != let2:
        b = 2
        print(b)

    if let1 == let2:
        b = 0
        print("coincidencia")
        print(b)
    
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        print("hehe")
        c = c + 1
        print(c)
 #   elif a == 1 and b == 2:


    x = x + 1
    print(" ")

print("EL numero de configuraciones validas fueron: ", c)