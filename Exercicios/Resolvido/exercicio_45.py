'''45 - Crie um programa que faça o computador jogar Jokenpô com você.

    - Pedra
    - Papel
    - Tesoura'''

import random
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
escolha = -1
while (escolha<0) or (escolha>2):
    escolha=int(input('Jokenpo!\nDigite 0 para Pedra\nDigite 1 para Papel\nDigite 2 para Tesoura\n\nEscolha: '))
'''if escolha==1:
    escolha=('Pedra')
elif escolha==2:
    escolha=('Papel')
else:
    escolha=('Tesoura')'''

jokenpo=random.randint(0,2)

'''if jokenpo == 1:
    computador='Pedra'
elif jokenpo == 2:
    computador='Papel'
else:
    computador='Tesoura'''

print('====================')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.7)
print('====================\n')

print('Você: {}'.format(itens[escolha]))
print('Computador: {}'.format(itens[jokenpo]))
print('\n====================')

if (escolha==0 and jokenpo==0) or (escolha==1 and jokenpo==1) or (escolha==2 and jokenpo==2):
    print('Empate')
elif (escolha==0 and jokenpo==2) or (escolha==1 and jokenpo==0) or (escolha==2 and jokenpo==1):
    print('Você venceu!')
else:
    print('Perdeu!')