from collections import defaultdict

versiones_lenguajes = defaultdict(lambda: '1.0.0')
versiones_lenguajes['Java'] = '12.0.0'
versiones_lenguajes['PHP'] = '7.1.2'
versiones_lenguajes['C#'] = '7.0.0'

print(len(versiones_lenguajes))
print(versiones_lenguajes)
print(versiones_lenguajes['Java'])
print(versiones_lenguajes['PHP'])
print(versiones_lenguajes['C#'])
print(versiones_lenguajes['Python'])

print()

lenguajes = 'Python JavaScript PHP C# Java C++ C PHP PHP Python Python JavaScript'
lenguajes = lenguajes.split()
print(lenguajes)

conteo_lenguajes = defaultdict(int)
for l in lenguajes:
    conteo_lenguajes[l] += 1

print(conteo_lenguajes)
print(conteo_lenguajes['Python'])
print(conteo_lenguajes['C'])
print(conteo_lenguajes['Kotlin'])

print()

# Crear un diccionario predeterminado con valores:
puntajes = defaultdict(int, Edward=80, Daniela=85, Oliva=90)
print(len(puntajes))
print(puntajes['Edward'])
print(puntajes['Daniela'])
print(puntajes['Oliva'])
print(puntajes['Germán'])

puntajes['Germán'] = 75
print(puntajes['Germán'])
