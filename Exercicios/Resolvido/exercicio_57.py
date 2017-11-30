# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
rotina = True

while rotina == True:
    sexo = input('Sexo (M) / (F): ').upper()
    if sexo in 'MF':
        rotina = False
    else:
        print('As opção são apenas M ou F')
