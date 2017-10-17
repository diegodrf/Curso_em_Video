'''1 - A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

    - Até 9 anos: MIRIM;
    - Até 14 anos: INFANTIL;
    - Até 19 anos: JUNIOR;
    - Até 20 anos: SÊNIOR;
    - Acima: MASTER;'''

idade=int(input('Idade do atleta: '))

if idade <= 9:
    print('MIRIM')
elif (idade > 9) and (idade <= 14):
    print('INFANTIL')
elif (idade > 14) and (idade <= 19):
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
else:
    print('MASTER')