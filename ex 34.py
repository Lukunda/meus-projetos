salário = int(input('Qual é o salário do funcionário?: '))
if salário > 1250:
    m = (salário * 10/100) + salário
else:
    salário <= 1250
    m = (salário * 15/100) + salário
print('O funcionário passou de R${:.2f}, para um salário de {:.2f}'.format(salário,m))