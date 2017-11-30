# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. Considere a maioridade em 21 anos.

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - nascimento >= 21:
        maior += 1
    else:
        menor += 1


print('Maiores de idade: {}\nMenores de dade: {}'.format(maior, menor))