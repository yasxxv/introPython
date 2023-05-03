#desafio 16
from math import hypot
n1 = int(input('comprimeto do cateto oposto: '))
n2 = int(input('comprimeto do cateto adiacente: '))
hi = hypot(n1,n2)
print('O numero digitado foi {:.2f}'.format(hi))