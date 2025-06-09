# Faça um programa que leia a largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta
# uma área de 2m2.

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
Area = largura * altura
quant_tinta = Area / 2

print(f'Area total {Area} metros quadrados e a quantidade de tinta é {quant_tinta}latas')
