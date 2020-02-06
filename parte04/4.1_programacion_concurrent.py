import gevent

def fn1():
    print('Inicio: fn1')
    gevent.sleep(0)
    print('Fin: fn1')

def fn2():
    print('Inicio: fn2')
    gevent.sleep(0)
    print('Fin: fn2')

def fn3():
    print('Inicio: fn3')
    gevent.sleep(0)
    print('Fin: fn3')

funciones = [gevent.spawn(fn1), gevent.spawn(fn2), gevent.spawn(fn3)]

gevent.joinall(funciones)
