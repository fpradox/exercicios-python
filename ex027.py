# Faça um programa que leia o nome completo de uma pessoa, montrando em seguida
# o primeiro e o último nome separadamente.
# # - O primeiro nome.

# nome = input('Digite seu nome completo: ').strip()
# primeiro_nome = nome.split()[0]
# ultimo_nome = nome.split()[-1]  
# print(f'Seu primeiro nome é: {primeiro_nome}')
# print(f'Seu último nome é: {ultimo_nome}')

nome = input('Digite seu nome completo: ').strip()
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]
print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu último nome é: {ultimo_nome}')
# - O último nome