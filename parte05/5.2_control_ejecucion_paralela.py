import multiprocessing

def retirar(saldo, lock):
    for i in range(2000):
        lock.acquire()
        saldo.value = saldo.value - 1
        lock.release()

def depositar(saldo, lock):
    for i in range(2000):
        lock.acquire()
        saldo.value = saldo.value + 1
        lock.release()

