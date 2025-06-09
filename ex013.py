# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15%
# de aumento.

sal_atual = float(input('Digite seu salário base: R$ '))
novo_sal = sal_atual + (sal_atual * 0.15)
print(f'Seu novo salário é: {novo_sal}')