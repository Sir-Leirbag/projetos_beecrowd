#Cálculo do consumo médio de um carro

#input
distancia = int(input('Digite a distância percorrida em Km: '))
combustivel = float(input('Digite o total de combustível gasto: '))

#processamento
media = distancia / combustivel

#output
print(f'Valor médio de consumo: {media:.3f} Km/l')
