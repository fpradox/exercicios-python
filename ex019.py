# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na 
# tela o nome do escolhido.

#Sorteio de alunos
import random

# Lista para armazenar o nome dos alunos
alunos  = []

# Lendo o nome dos quadros alunos
print("--- Sorteio de Alunos ---")
alunos.append(input("Digite o nome do 1o. aluno:"))
import random

# Lista para armazenar o nome dos alunos
alunos = []

# Lendo o nome dos quatro alunos
print("--- Sorteio de Alunos ---")
alunos.append(input("Digite o nome do 1º aluno: "))
alunos.append(input("Digite o nome do 2º aluno: "))
alunos.append(input("Digite o nome do 3º aluno: "))
alunos.append(input("Digite o nome do 4º aluno: "))

# Sorteando um aluno da lista
aluno_escolhido = random.choice(alunos)

# Exibiando o nome do aluno sorteado
print(f'\nO Aluno escolhido para apagar o quadro foi: {aluno_escolhido}')






