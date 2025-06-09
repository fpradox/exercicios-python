# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ele pode comprar.

# Considere 
# U$ 1.00 = R$ 5.56 - cotação do dia 

dinheiro_cart = float(input('Quanto de dinheiro tem na carteira para comprar dolar?'))
qtd_dollar = dinheiro_cart / 5.56
print(f'Voce consegue comprar {qtd_dollar:.2f} dólares')










