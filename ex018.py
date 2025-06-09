# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno,
# cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite um ângulo em graus: "))
rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f"O ângulo de {angulo}° tem o SENO de {seno:.4f}")
print(f"O ângulo de {angulo}° tem o COSSENO de {cosseno:.4f}")
print(f"O ângulo de {angulo}° tem a TANGENTE de {tangente:.4f}")