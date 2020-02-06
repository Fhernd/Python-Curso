import cProfile

def insercion():
    arr = [64, 25, 12, 22, 11]
    for i in range(1, len(arr)): 
    
        key = arr[i] 
    
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key


cProfile.run('insercion()')
