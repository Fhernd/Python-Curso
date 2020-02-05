from collections import Counter
import numpy as np
from scipy import stats

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

print()

# Otras operaciones estadísticas:

promedio = np.mean(conteos)
mediana = np.median(conteos)
minimo = np.min(conteos)
maximo = np.max(conteos)

print('Promedio: %f' % promedio)
print('Mediana: %f' % mediana)
print('Mínimo: %f' % minimo)
print('Máximo: %f' % maximo)

print()

moda = stats.mode(conteos)
print('Moda: {}'.format(moda.mode[0]))
