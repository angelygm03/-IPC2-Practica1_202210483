import os

class Producto:
    def __init__(self, codigoProducto, nombreProducto, descripcionProducto, precioUnitario):
        self.codigoProducto = codigoProducto
        self.nombreProducto = nombreProducto
        self.descripcionProducto = descripcionProducto
        self.precioUnitario = precioUnitario  

class Cliente:
    def __init__(self, nombreCliente, correo, nit):
        self.nombreCliente = nombreCliente
        self.correo = correo
        self.nit = nit

class Compra:
    def __init__(self, id_compra, productos, clientes, costo_total):
        self.id_compra = id_compra
        self.productos = productos
        self.cliente = clientes
        self.costo_total = costo_total
        self.impuesto = costo_total * 0.12

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

#listas
productos = []
clientes = []

def main():
    print("     Bienvenido a Uolmart    ")
    print(" Menú principal")
    print("1. Registrar productos")
    print("2. Registrar cliente")
    print("3. Realizar compra")
    print("4. Reporte de compra")
    print("5. Datos del estudiante")
    print("6. Salir")
    respuesta = input("Ingresa la acción que quieras realizar: ")

    if respuesta =="1":
        registrar_producto()
    elif respuesta == "2":
        registrar_cliente()
    elif respuesta == "3":
        realizar_compra()
    elif respuesta == "4":
        realizar_reporte()
    elif respuesta == "5":
        print()
        print("----------- Datos Personales ----------")
        print("Nombre: Angely Lucrecia García Martínez")
        print("Carnet: 202210483")
        print("---------------------------------------")
        print()
        main()
    elif respuesta == "6":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Inténtalo de nuevo")
        main() 

def registrar_producto():
    limpiar_pantalla()
    codigoProducto = input("Ingrese el código del producto: ")
    nombreProducto = input("Ingrese el nombre del producto: ")
    descripcionProducto = input("Ingrese la descripcion del producto: ")
    while True:
        try:
            precioUnitario = float(input("Ingrese el precio unitario del producto: "))
            break
        except ValueError:
            print("El precio ingresado no es válido. Intente nuevamente.")
    
    producto = Producto(codigoProducto, nombreProducto, descripcionProducto, precioUnitario)
    productos.append(producto)
    print(productos) #apuntador del producto en la lista
    print()
    print("¡Producto registrado con éxito!")
    print()
    print("1. Registrar nuevo producto")
    print("2. Volver al menú principal")
    print("3. Salir")
    repetirRegistro = input("Ingrese su respuesta: ")
    if repetirRegistro == "1":
        registrar_producto()
    elif repetirRegistro == "2":
        main()
    elif repetirRegistro == "3":
        print("¡Hasta luego!")
    else:
        print("Respuesta inválida. Intente de nuevo")
        repetirRegistro()


def registrar_cliente():
    nombreCliente = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    while True:
        try:
            nit = int(input("Ingrese el NIT del cliente: "))
            break
        except ValueError:
            print("El NIT ingresado no es válido. Intente nuevamente.")
    for cliente in clientes:
        if cliente.nit == nit:
            print("Error: El NIT ingresado ya está registrado para otro cliente.")
            print("Por favor, ingrese un NIT diferente.")
            return registrar_cliente()    
    cliente = Cliente(nombreCliente, correo, nit) 
    clientes.append(cliente)
    print(clientes)
    print("¡Cliente registrado con éxito!")
    print()
    print("1. Registrar nuevo cliente")
    print("2. Volver al menú principal")
    print("3. Salir")
    agregarCliente = input("Ingrese su respuesta: ")
    if agregarCliente == "1":
        registrar_cliente()
    elif agregarCliente == "2":
        main()
    elif agregarCliente == "3":
        print("¡Hasta luego!")
    else:
        print("Respuesta inválida. Intente de nuevo")
        agregarCliente()


def realizar_compra():
    limpiar_pantalla()
    print("Menú Compra")
    print("1. Agregar producto")
    print("2. Terminar compra y facturar")
    seleccion_compra = input("Ingrese la acción a realizar: ")
    if seleccion_compra == "1":
        print("Clientes registrados: ")
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. Nombre: {cliente.nombreCliente}, Correo: {cliente.correo}, NIT: {cliente.nit}")
        while True:
            try:
                nit_cliente = int(input("Ingrese el NIT del cliente: "))
                cliente_seleccionado = None
                for cliente in clientes:
                    if cliente.nit == nit_cliente:
                        cliente_seleccionado = cliente
                        break
                if cliente_seleccionado is None:
                    raise ValueError("El NIT ingresado no corresponde a ningún cliente registrado.")
                break
            except ValueError as e:
                print(str(e))
        
        print("Productos disponibles:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Código: {producto.codigoProducto}, Nombre: {producto.nombreProducto}, Precio: {producto.precioUnitario}")
        
        productos_a_comprar = []
        while True:
            seleccion_producto = input("Ingrese el número de producto a comprar (0 para terminar): ")
            if seleccion_producto == '0':
                break
        try:
            indice_producto = int(seleccion_producto) - 1
            producto_seleccionado = productos[indice_producto]
            productos_a_comprar.append(producto_seleccionado)
        except (ValueError, IndexError):
            print("Selección inválida.")
        realizar_compra()
        costo_total = sum(producto.precioUnitario for producto in productos_a_comprar)
        compra = Compra(id_compra = 1, productos = productos_a_comprar, clientes = cliente_seleccionado, costo_total = costo_total)
    elif seleccion_compra == "2":    
        print("Detalles de la compra:")
        print("Cliente:", compra.cliente.nombreCliente)
        print("Productos:")
        for i, producto in enumerate(compra.productos, start=1):
            print(f"{i}. Código: {producto.codigoProducto}, Nombre: {producto.nombreProducto}, Precio: {producto.precioUnitario}")
        print("Costo Total:", compra.costo_total)
        print("Impuesto (12%):", compra.impuesto)
        main()

def realizar_reporte():
    limpiar_pantalla()
    print("Generar reporters")

main()



