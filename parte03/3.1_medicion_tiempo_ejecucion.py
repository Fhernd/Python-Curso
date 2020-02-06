from timeit import timeit

inicializacion = 'from math import sqrt'
codigo = '''
raices = []
for i in range(100):
    raices.append(sqrt(i))
'''

print(timeit(setup=inicializacion, stmt=codigo, number=10000))
