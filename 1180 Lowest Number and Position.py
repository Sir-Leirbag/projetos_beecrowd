#Escreva um programa que leia um número N. 
# Este N é o tamanho de um vetor X[N]. 
# Em seguida, leia cada um dos números de X, 
# encontre o menor elemento desse vetor e sua posição dentro do vetor, 
# imprimindo essa informação.

numero = int(input('Digite um número: '))
sequencia = input(f'Digite {numero} números separados por espaço: ').split()

menor_valor = min(sequencia)
posicao = sequencia.index(menor_valor) + 1

print(f'\nMenor valor = {menor_valor}')
print(f'Posição = {posicao}')
