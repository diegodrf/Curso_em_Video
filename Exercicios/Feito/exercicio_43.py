'''43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tablea abaixo:

    - Abaixo de 18.5: Abaixo do Peso;
    - Entre 18.5 e 25: Peso ideal;
    - 25 até 30: Sobrepeso;
    - 30 até 40: Obesidade]
    - Acima de 40: Obesidade mórbida;'''

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5<= imc <25:
    print('Peso ideal')
elif 25<= imc <30:
    print('Sobre peso')
elif 30 <= imc <40:
    print('Obesidade')
elif 40 < imc:
    print('Obesidade mórbida')