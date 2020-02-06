import multiprocessing

def retirar(saldo, lock):
    for i in range(500):
        lock.acquire()
        saldo.value = saldo.value - 1
        lock.release()

def depositar(saldo, lock):
    for i in range(2000):
        lock.acquire()
        saldo.value = saldo.value + 1
        lock.release()

def ejecutar_transacciones():
    saldo = multiprocessing.Value('i', 1000)
    lock = multiprocessing.Lock()

    proceso_1 = multiprocessing.Process(target=retirar, args=(saldo, lock))
    proceso_2 = multiprocessing.Process(target=depositar, args=(saldo, lock))

    proceso_1.start()
    proceso_2.start()

    proceso_1.join()
    proceso_2.join()

    print('Saldo final: %i' % saldo.value)


if __name__ == "__main__":
    for i in range(10):
        ejecutar_transacciones()
