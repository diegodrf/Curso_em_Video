# Crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços.
# Ex.:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Informe uma frase: ')).replace(' ','').upper()
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
print('\nFrase original:  {}\nFrase invertida: {}'.format(frase, frase_invertida))