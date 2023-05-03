#desafio 15
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foi rodado? '))
preco = (dias * 60) + (km * 0.15)
print('O valor a ser pago é R${:.2f}'.format(preco))