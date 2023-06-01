print('-='*20)
print('Analisador de triangulos')
print('-='*20)
l1 = float(input('primeiro segmento: '))
l2 = float(input('segundo segmento: '))
l3 = float(input('terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('o triangulo existe')
else:
    print('o triangulo não existe')


