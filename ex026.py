# Faça um progama que leia uam frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a ultima vez."

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))  # Conta quantas vezes 'A' aparece na frase
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))  # +1 para ajustar ao índice humano
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))  # +1 para ajustar ao índice humano                                                                 