""""
A person invests $1000 in a savings account yielding 
5% interest.
Assuming that the person leaves all interest on
deposit in the account, calculate and display the
amount of money in the account at the end of each
year for 10 years.

            a=p(1+r)**n

a = amount on deposit at the end of the nth year
p = ORIGINAL AMOUNT invested (i.e. the principal)
r = annual interest RATE
n = number of the YEARS
"""

from decimal import Decimal

## En este caso solo se va a importar el modulo Decimal de
## la libreria decimal

p = Decimal('1000.00')
r = Decimal('0.05')

for n in range(1,11):
    a = p* (1 + r) ** n
    #print(a)
    print(f'{n:>2}{a:>10.2f}')

"""
¿Qué significa el ultimo print?

n:>2 => 
"""