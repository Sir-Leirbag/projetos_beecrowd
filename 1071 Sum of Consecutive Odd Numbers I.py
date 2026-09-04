#Leia dois valores inteiros X e Y. Imprima a soma de todos os valores ímpares entre eles.

sequencia = []
impares = []

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

sequencia.append(numero1)
sequencia.append(numero2)

for i in range (min(sequencia) + 1, max(sequencia)):
    if i % 2 != 0:
        impares.append(i)

print(f'A soma dos números ímpares é: {sum(impares)}')
