#Entrada de datos
cliente = input('Nombre del cliente: ')
producto = input('Producto a pagar: ')
cantidad = int(input('Cantidad a llevar: '))
precio = float(input('Costo de producto: '))

#Calculos correspondientes y constantes
IVA = 0.16
Descuento = 0.10
costo = precio * cantidad
descuento = costo * (1-Descuento)
total = descuento * (1+IVA)

#Estructura del ticket + decoración
print('\nCliente: ', cliente)
print('-------------------------------------')
print('Producto a pagar: ', producto, '\nCantidad a llevar: ', cantidad)
print('Precio del producto: $', precio)
print('(+) IVA: ', IVA)
print('Total: $', total)
print('-------------------------------------')
#Cliente (nombre),producto, precio, cant de productos
#precio tipo float, cantidad tipo int
#Constantes iva = 0.16 y descuento = 0.10
#subtotal de compra, monto de descuento, iva y total, funcion type (tres)
