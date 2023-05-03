#defio 4
x = input('Digite algo: ')
print('Qual é o tipo primitivo desse valor?', type(x))
print('Possui apenas espaços? {}'.format (x.isspace()))
print('Possui apenas letras? {}'.format (x.isalpha()))
print('Possui apenas Numeros? {}'.format (x.isnumeric()))
print('Possui apenas Numeros ou Letras? {}'.format (x.isalnum()))
print('Possui apenas Letras maiúsculas? {}'.format (x.isupper()))
print('Possui apenas Letras minúsculas? {}'.format (x.islower()))
print('Esta capitalizada? {}'.format (x.istitle()))#capitalizada ---> não maiuscula e nem minuscula 