'''45 - Crie um programa que faça o computador jogar Jokenpô com você.

    - Pedra
    - Papel
    - Tesoura'''

import random

escolha=-1
while (escolha<0) or (escolha>3):
    escolha=int(input('Jokenpo!\nDigite 1 para Pedra\nDigite 2 para Papel\nDigite 3 para Tesoura\n\nEscolha: '))
if escolha==1:
    print('Você: Pedra')
elif escolha==2:
    print('Você: Papel')
else:
    print('Você: Tesoura')

jokenpo=random.randint(1,3)

if jokenpo == 1:
    computador='Pedra'
elif jokenpo == 2:
    computador='Papel'
else:
    computador='Tesoura'

print('Computador: {}'.format(computador))

if (escolha==1 and jokenpo==1) or (escolha==2 and jokenpo==2) or (escolha==3 and jokenpo==3):
    print('Empate')
elif (escolha==1 and jokenpo==3) or (escolha==2 and jokenpo==1) or (escolha==3 and jokenpo==2):
    print('Você venceu!')
else:
    print('Perdeu!')