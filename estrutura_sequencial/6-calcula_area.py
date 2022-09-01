from math import pi


def calcula_area():
    raio = float(input('Insira o raio do circulo: '))
    return f"{raio**2 * pi:.2f}"

print(calcula_area())