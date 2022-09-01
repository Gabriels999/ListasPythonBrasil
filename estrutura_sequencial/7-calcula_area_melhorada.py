from math import pi


def calcula_area():
    raio = float(input('Insira o raio do circulo: '))
    area = raio**2 * pi
    return f"{area**2:.2f}"

print(calcula_area())