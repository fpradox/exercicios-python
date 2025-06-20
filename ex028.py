# # Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5]
# # e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# # O programa deverá escrever na tela se o usuário venceu ou perdeu.
# import random
# numero = random.randint(0,5)  # Gera um número aleatório entre 0 e 5
# tentativa = int(input('Tente adivnhar o numero  entre 0 e 5: '))
# if tentativa == numero:
#     print(f'Parabéns! Você acertou, o número era {numero}.')
# else:
#     print(f'Você errou! O número era {numero}. Tente novamente.')   

from random import randint
from time import sleep
computador = randint(0, 5)  # O computador escolhe um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar: ')
print('-=-' * 20)
jogador = int(input("Em que númerou eu pensei?")) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)  # Pausa de 3 segundos para aumentar a expectativa
if jogador == computador:
    print(f'Parabéns! Você acertou, o número era {computador}.')
else:
    print(f'Você errou! O número era {computador}. Tente novamente.')



