'''39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

    - Se ele ainda vai se alistar ao serviço militar;
    - Se é a hora de se alistar;
    - Se já passou do tempo do alistamento;

  Seu programa também deverámostrar o tempo que falta ou que passou do prazo.'''

import datetime
ano = datetime.date.today().year

nascimento=int(input('Em que ano você nasceu? '))

idade = ano - nascimento
print(idade)
if idade < 17:
    tempo = 17 - idade
    print('Faltam {} anos para você se alistar'.format(tempo))
elif idade == 17:
    print('Você se alistará esse ano')
else:
    tempo = idade - 17
    print('Você está {} anos atrasado para o alistamento'.format(tempo))