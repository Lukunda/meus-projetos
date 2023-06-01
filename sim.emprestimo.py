empréstimo = float(input('valor da casa: R$'))
salário = float(input('salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
cf = (0.015)/1-(1+0.015) ** financiamento
prestação = financiamento * cf
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(empréstimo,financiamento,prestação))
print('Empréstimo NEGADO!{}')
