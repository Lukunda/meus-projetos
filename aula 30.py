número = int(input('Me diga um número: '))
valor = número % 2
if valor == 0:
    print ('o número {} é par'.format(número))
else:
    print('o número {} é impar'.format(número))