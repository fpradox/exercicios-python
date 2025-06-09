# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela 
# a sua porção inteira.
import math

# Solicitar ao usuario que digite um numero real
num = float(input('Digite um numero real:'))

# obtem a parte inteira usando math.trunc()
parte_inteira = math.trunc

#Mostra o resultado
print(f"a parte inteira de {num} é {math.trunc(num)}")