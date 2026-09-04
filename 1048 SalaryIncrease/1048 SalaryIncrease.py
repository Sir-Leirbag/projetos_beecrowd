#funções
def calcular_novo_salario(salario, percentual_decimal):
    return (salario + (salario * percentual_decimal))

def calcular_reajuste(salario, percentual_decimal):
    return (salario * percentual_decimal)

def exibir_mensagem(salario, percentual_decimal, percentual):
    print(f'Novo salário: R$ {calcular_novo_salario(salario_atual, percentual_decimal):.2f}')
    print(f'Reajuste ganho: R$ {calcular_reajuste(salario_atual, percentual_decimal):.2f}')
    print(f'Em percentual: {percentual}%')

#input
salario_atual = float(input('Digite o valor do salário atual: '))

#processamento
if 0 < salario_atual <= 400:
    exibir_mensagem(salario_atual, 0.15, 15)
elif 400 < salario_atual <= 800:
    exibir_mensagem(salario_atual, 0.12, 12)
elif 800 < salario_atual <= 1200:
    exibir_mensagem(salario_atual, 0.10, 10)
elif 1200 < salario_atual <= 2000:
    exibir_mensagem(salario_atual, 0.07, 7)
elif salario_atual > 2000:
    exibir_mensagem(salario_atual, 0.04, 4)
else:
    print('valor inválido.')
