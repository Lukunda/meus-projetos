viagem = float(input('Qual é a distância da sua viagem?: '))
print('você está prestes a começar uma viagem de {:.1f} km'.format(viagem))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45

print('e o preço da sua passagem será de R${:.2f}'.format(preço))