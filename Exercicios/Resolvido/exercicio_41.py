'''1 - A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

    - Até 9 anos: MIRIM;
    - Até 14 anos: INFANTIL;
    - Até 19 anos: JUNIOR;
    - Até 25 anos: SÊNIOR;
    - Acima: MASTER;'''
from datetime import date
ano_atual = date.today().year

ano_nasc=int(input('Ano de nascimento: '))

idade = ano_atual - ano_nasc

if idade <= 9:
    print('MIRIM')
elif (idade > 9) and (idade <= 14):
    print('INFANTIL')
elif (idade > 14) and (idade <= 19):
    print('JUNIOR')
elif 19 < idade <=25:
    print('SENIOR')
else:
    print('MASTER')