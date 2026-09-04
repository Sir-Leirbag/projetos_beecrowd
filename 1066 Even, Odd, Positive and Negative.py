# Conta quantos valores são pares, ímpares, positivos e negativos.

numeros = []
impares = []
pares = []
positivos = []
negativos = []

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    if numero > 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print(f'\n{len(pares)} valor(es) par(es)')
print(f'{len(impares)} valor(es) impar(es)')
print(f'{len(positivos)} valor(es) positivo(s)')
print(f'{len(negativos)} valor(es) megativo(s)')
