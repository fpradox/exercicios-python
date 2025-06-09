# Escreva um programa que pergunte a quantidadede km percorridos por um carro
# de aluguel e a quantidade de dias pelos quais ele foi alugado. Calcule 
# o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.


dias_aluguel = int(input('Digite a quantidade de dias da locação do veiculo:'))
km_rodado = float(input('Qual a quantidade de quilômetros percorridos: '))
total_dias = dias_aluguel * 60
total_km = km_rodado * 0.15
total_pagar = total_dias + total_km
print(f' Valor total a ser pago: R${total_pagar:.2f}')