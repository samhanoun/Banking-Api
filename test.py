from datetime import date, timedelta
from random import randint


nombres = [2,3,4,5,6,7,8,9]
carres = [nombre ** 2 for nombre in nombres if nombre % 2 == 0]
carres = [nombre ** 2 if nombre % 2 == 0 else nombre ** 3 for nombre in nombres ]

numero = ''.join([str(randint(0, 9)) for i in range(16)])

# XXXX XXXX XXXX XXXX
print(numero)
print(numero[0:4])
print(numero[4:8])
print(numero[8:12])
print(numero[12:16])

print(' '.join([numero[i: i+4] for i in range(0, 13, 4)]))

# destructuring data
infos = ('John', 'Doe', 34)
prenom = infos[0]
nom = infos[1]
age = infos[2]

prenom, _, age = infos

from dateutil.relativedelta import relativedelta

auj = date.today()
(auj + relativedelta(years= 5)).strftime('%m/%y')