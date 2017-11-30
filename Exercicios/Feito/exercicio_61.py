# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura WHILE.

num = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

termo = 1
while termo < 11:
    print('{}'.format(num), end=' > ')
    num += razao
    termo += 1
print('FIM')