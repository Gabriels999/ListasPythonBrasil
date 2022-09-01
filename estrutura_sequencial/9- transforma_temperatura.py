def transforma_temperatura():
    faren = float(input('Insira a temperatura em Fahrenheit: '))
    return 5*((faren-32)/9)

print(transforma_temperatura())