# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retangulo. Calcule o comprimento da hipotenusa

# ca = float(input('Digite o valor do cateto adjacente: '))
# co = float(input('Digite o valor do cateto oposto: '))
# hp = (ca*ca + co * co) ** 0.5
# print("O valor da hipotenusa  é : ",hp)

import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

hp = math.hypot(ca, co)
print(f"A hipotenusa é: {hp}")