# Faça um programa que leia algo pelo teclado e mostre na tela  o seu tipo
# primitivo  e todas as informações possíveis sobre ele

algo = input('Digite algo para validar o tipo primitivo: ')
print('O tipo desse valor é: ', type(algo))  
print('Só tem espaços?', algo.isspace()) 
print('É numérico?', algo.isnumeric()) 
print('é alfabético?',algo.isalpha())
print('é alfanumérico?',algo.isalnum())
print('Está em maiúsculas',algo.isupper())
print('Esta em minusculas',algo.islower())
print('Está capitalizada',algo.istitle())