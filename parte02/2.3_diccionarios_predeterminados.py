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
