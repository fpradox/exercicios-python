# O mesmo professor do desfio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle # Importa a biblioteca random para operações de sorteiro
aluno1 = str(input('Digite o nome do aluno 1o. '))
aluno2 = str(input('Digite o nome do aluno 2o. '))
aluno3 = str(input('Digite o nome do aluno 3o. '))
aluno4 = str(input('Digite o nome do aluno 4o. '))

# colodando o nome dos alunos em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteando a ordem dos alunos
shuffle(alunos)


# Exibindo a ordem sorteada
print("\n-- Ordem de apresentação Sorteada ---")
for i, aluno in enumerate(alunos): # Usamos enumerate para ter a posição (1o., 2o., etc)
    print(f"i + 1)o. - {aluno}")       
    

