# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro (km/h): '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f'Você foi multado! A multa é de R$ {multa:.2f} por exceder {excesso:.2f} km/h do limite de 80 km/h.')
print    
