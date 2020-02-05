from collections import Counter
import numpy as np

lista_letras = ['t', 'u', 't', 'w', 'x', 'x', 'w', 't', 'y', 'y', 'z']
contador = Counter(lista_letras)
print(contador)

print()

dict_letras = {'t': 3, 'u': 1, 'w': 2, 'x': 2, 'y': 2, 'z': 1}
contador = Counter(dict_letras)
print(contador)

print()

contador = Counter(t= 3, u=1, w=2, x=2, y=2, z=1)
print(contador)

print()

cadena = 'tutwxxwtyyz'
contador = Counter(cadena)
print(contador)

print()

print(contador['x'])
print(contador.most_common(3))

print()

for k, v in contador.most_common():
    print('Llave: {} - Valor: {}'.format(k, v))

print()

conteos = [v for k, v in contador.most_common()]
print(len(conteos))
print(conteos)
