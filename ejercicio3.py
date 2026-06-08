#Identificadores y vaiables
#variables con snake_case
#Quiero obtener el nombre de un alumno, ¿cómo debo definir mi identificador?
nombre_alumno = 'Gissel Cornelio'
edad_alumno = 18
promedio_final = 9.5

#Constantes con SCREAMING_SNAKE_CASE
TASA_IVA = 0.16
CALIFICACION_MINIMA = 7
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25

#Tipado dinamico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = 'cien'
print(type(dato))

#Uso de constantes en un cálculo
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)
print(f'Precio con IVA: ${precio_final:.2f}')
#2f: Para el numero de decimales despues del punto/ f: realiza la conversion dentro del print

#Tres constantes, PESO_PARCIAL=0.20 PESO_PROYECTO=0.40, y CALIFICAION_MINIMA=6.0 
# Luego crea 4 variables con calificaciones y calcula el promedio 
# usando las constantes. Imprime si el alumno aprobó o reprobó
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0
cal_1 = 10
cal_2 = 9
cal_3 = 9
cal_4 = 10
promedio_final = (cal_1 + cal_2 + cal_3 + cal_4)/4
mensaje = 'Promedio final: ' + str(promedio_final)
print(mensaje)
print('Estado: ' + 'Aprobado'if promedio_final >= CALIFICACION_MINIMA else 'Reprobado' ) 