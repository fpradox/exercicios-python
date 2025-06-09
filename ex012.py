# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5%
# de desconto.

# Programa Desconto

preco_prod = float(input('Digite o preço do produto: R$ '))
desconto = preco_prod * 0.05
novo_preco = preco_prod - desconto

print(f'O desconto foi de R$ {desconto:.2f}')
print(f'O preço com 5% de desconto é: R$ {novo_preco:.2f}')