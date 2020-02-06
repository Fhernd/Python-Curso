from multiprocessing import Pool

def cubo(n):
    n += 1
    resultado = n ** 3
    return resultado

print(Pool().map(cubo, [2, 3, 5]))
