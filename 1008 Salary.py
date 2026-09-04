#Cálculo do salário a partir do valor da hora
#e do número de horas trabalhadas

#input
matricula = input('Digite a matricula: ')
horas = int(input('Digite o número de horas trabalhadas: '))
valor = float(input('Digite o valor da hora trabalhada: '))

#processamento
total = horas * valor

#output
print(f'\nMatrícula: {matricula}')
print(f'Total a receber: R$ {total:.2f}')
