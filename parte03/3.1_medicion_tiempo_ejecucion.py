from timeit import timeit

inicializacion = 'from math import sqrt'
codigo = '''
raices = []
for i in range(100):
    raices.append(sqrt(i))
'''

print(timeit(setup=inicializacion, stmt=codigo, number=10000))

codigo = '''
raices = []
raices = [lambda i: sqrt(i) for i in range(100)]
'''

print(timeit(setup=inicializacion, stmt=codigo, number=10000))

print()

# Comparación algoritmos de ordenamiento: Selección vs. Inserción

codigo_seleccion = '''
A = [64, 25, 12, 22, 11] 
  
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    A[i], A[min_idx] = A[min_idx], A[i]
'''

codigo_insercion = '''
arr = [64, 25, 12, 22, 11]
for i in range(1, len(arr)): 
  
    key = arr[i] 
  
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key
'''

print(timeit(stmt=codigo_seleccion, number=1000000))
print(timeit(stmt=codigo_insercion, number=1000000))
