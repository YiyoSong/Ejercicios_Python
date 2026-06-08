#- Casting básico
# Implicita: int + float = float automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#Explicita: str a int
texto_numero = '42'
numero_real = int(texto_numero)
print(numero_real + 8)

#Explicita: int a str para concatenar

edad = 18
mensaje = 'Hola, soy Gissel y yo tengo ' + str(edad) + ' años'
print(mensaje)

#float a int
precio = 9.99
print(int(precio))

numero = 7.99
redondeado = round(numero)
print(redondeado)

# Simularemos input con variables fijas
dato_usuario = '25'
print(type(dato_usuario))
#print(dato_usuario + 5)
edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#patron correcto para entrada de datos
#edad = int(input('Ingresa tu edad: '))

#Programa
nombre =  input('Ingrese su nombre: ')
año_de_nacimiento  = int(input('Ingrese su fecha de nacimiento: '))
correct_age = int(año_de_nacimiento) 
print(2026 - correct_age)
