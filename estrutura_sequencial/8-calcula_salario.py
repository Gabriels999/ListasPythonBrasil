def calcula_salario():
    valor_hora = float(input('Digite o valor da sua hora: '))
    horas = float(input('Digite as horas trabalhadas: '))
    return valor_hora*horas

print(calcula_salario())