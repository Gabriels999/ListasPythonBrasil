def calcula_media():
    soma = 0
    for _ in range(4):
        soma+= float(input('Digite uma nota: '))
    return soma/4

print(calcula_media())