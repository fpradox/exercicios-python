# Criee um programa que leia o nome de uma pessoa e diga se ela tem "silva" no
#nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.upper())) # Verifica se 'SILVA' está no nome, ignorando maiúsculas/minúsculas.

