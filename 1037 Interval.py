#Você deve criar um programa que leia um número de ponto flutuante
#e imprima uma mensagem indicando em qual dos seguintes intervalos
#o número se enquadra: [0, 25], (25, 50], (50, 75], (75, 100].

#funções
def mensagem(intervalo):
    print(f'O número pertence ao intervalo: {intervalo}')

#input
numero = float(input('Digite um número de 1 a 100: '))

#processamento
if 1 <= numero <= 25:
    mensagem('[0,25]')
elif 25 < numero <= 50:
    mensagem('(25, 50]')
elif 50 < numero <= 75:
    mensagem('(50, 75]')
elif 75 < numero <= 100:
    mensagem('(75, 100]')
else:
    print('Fora de intervalo')
