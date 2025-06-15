# faça um programa que leia um número de 0 ate 9999 e mostre na tela cadda
# cada um dos digitos separados.
numint = int(input('Informe um número: '))
num = str(numint)  # Converte para string para acessar cada dígito

# Preenche com zeros à esquerda para garantir 4 dígitos
num = num.zfill(4)

print('Analisando o número {}'.format(numint))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
