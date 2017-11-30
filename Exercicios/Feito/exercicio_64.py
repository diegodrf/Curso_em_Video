# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
# o flag)
flag = True
soma = 0
contagem = 0
while flag == True:
    num = int(input('Informe um número (999 encerra): '))
    if num == 999:
        flag = False
    else:
        soma += num
        contagem += 1
print('A soma de todos os números é: {}'.format(soma))
print('Você digitou {} números'.format(contagem))