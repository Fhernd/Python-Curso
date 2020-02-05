numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(type(numeros))
print(len(numeros))
print(numeros)

print()

pares_triplicados = []

for n in numeros:
    if n % 2 == 0:
        pares_triplicados.append(n * 3)

print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)

print()

pares_triplicados = [n * 3 for n in numeros if n % 2 == 0]
print(type(pares_triplicados))
print(len(pares_triplicados))
print(pares_triplicados)
