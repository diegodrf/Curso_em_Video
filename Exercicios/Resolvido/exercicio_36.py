'''36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))

parcela_total = anos * 12
prestacao = valor_casa / parcela_total

limite_emprestimo = ( salario * 30 ) / 100

if prestacao > limite_emprestimo:
    print('A prestação ficará no valor de {:.2f}. Isso é maior do que 30% do seu salário.\nEMPRÉSTIMO NEGADO!'.format(prestacao))
else:
    print('A casa sairá por {}x de R$ {:.2f}.'.format(parcela_total,prestacao))