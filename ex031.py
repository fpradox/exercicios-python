# Desenvolva um programa que pergunta a distãncia de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM e 
# RS 0,45 para viagens mais longas. 

Kilometros_Viagem = float(input('Digite a quantidade de kilometros da Viagem: '))
if Kilometros_Viagem <= 200:
    valor_distancia = (Kilometros_Viagem * 0.50)
else:
    valor_distancia = (Kilometros_Viagem * 0.45) 
print(f'O valor a ser pago é R${valor_distancia:.2f}')                
             