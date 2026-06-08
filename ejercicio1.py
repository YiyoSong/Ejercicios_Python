#Este es un comentario de una línea

#Este es un comentario
#Que ocupa varias lineas

"""Este es otro ejemplo de
comentario multilinea"""

'''Este es otro ejemplo
de comentario multilinea'''


entero = 42 #Numeros enteros
decimal = 3.1416 #Numeros decimales (Float)
logico = True #Boolean
nombre = "Juan" #String

print(entero)
print(type(decimal))
print(type(logico))
print(type(nombre))
#Declara variables que almacene su nombre, apellidos, edad
name = "Gissel Estefania"
paternal_surname = "Cornelio"
maternal_surname = "Estrella"
age = 18
height = 1.58

print(paternal_surname)
print(maternal_surname)
print(name)
print(age)
print(height)

#list, tuple, set, dict, arrays, range, frozenset, nontype, complex

#Str - inm
nombreMateria = "Programación"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#list - mutable
calificaciones = [8.5, 9.0, 7.5, 10.0]
calificaciones.append(9.5)
calificaciones[0] = 8.0
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4326, -99.1332)
print(coordenadas[0])

# dict - clave:valor
alumno = {"nombre": 'Gissel', 'edad': 18, 'promedio': 9.5}
print(alumno['nombre'])
alumno['promedio'] = 9.6
print(alumno)
dictionary = {'last_name': 'Cornelio', 'name': 'Gissel', 'age': 18, 'favorite_subject': 'Maths'}
print(dictionary['name'])