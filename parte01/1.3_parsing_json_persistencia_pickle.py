import json
import pickle

datos = {}
datos['programadores'] = []

edward = {'id': 1001, 'nombre': 'Edward', 'apellido': 'Ortiz', 'especialidad': 'front-end', 'lenguaje': 'JavaScript', 'email': 'edward@mail.co'}

oliva = {'id': 1002, 'nombre': 'Oliva', 'apellido': 'Ordoñez', 'especialidad': 'back-end', 'lenguaje': 'Java', 'email': 'oliva@mail.co'}

juan = {'id': 1003, 'nombre': 'Juan', 'apellido': 'Urbano', 'especialidad': 'front-end', 'lenguaje': 'JavaScript', 'email': 'juan@mail.co'}

datos['programadores'].append(edward)
datos['programadores'].append(oliva)
datos['programadores'].append(juan)

print(len(datos['programadores']))

with open('parte01/programadores.json', 'w') as f:
    json.dump(datos, f)
