# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre;
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

media = 0
mulher_menor = 0
homem_idade_maisvelho = 0
for c in range(1, 5):
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).upper()

    if sexo == 'M':
        if idade > homem_idade_maisvelho:
            homem_nome = nome
            homem_idade_maisvelho = idade

    elif sexo == 'F':
        if idade < 20:
            mulher_menor += 1

    media += idade

media = media / 4

print('Idade média: {:.0f} anos'.format(media))
print('O homem mais velho é: {}'.format(homem_nome))
print('Mulheres com menos de 20 anos: {}'.format(mulher_menor))