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
        self.compras = []  

    def agregar_compra(self, compra):
        self.compras.append(compra)

class Compra:
    contador_facturas = 0
    def __init__(self, productos, cliente, costo_total):
        Compra.contador_facturas += 1
        self.id_compra = Compra.contador_facturas
        self.productos = productos
        self.cliente = cliente
        self.costo_total = costo_total
        self.impuesto = costo_total * 0.12

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

productos = []
clientes = []
compras = []
facturas = []

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
        realizar_compra(compras)
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
    codigoProducto = input("Ingrese el código del producto: ")
    for producto in productos:
        if producto.codigoProducto == codigoProducto:
            print("Error: Ya existe un producto con ese código.")
            return registrar_producto()
    nombreProducto = input("Ingrese el nombre del producto: ")
    descripcionProducto = input("Ingrese la descripcion del producto: ")
    while True:
        try:
            precioUnitario = float(input("Ingrese el precio unitario del producto Q."))
            break
        except ValueError:
            print("El precio ingresado no es válido. Intente nuevamente.")
    
    producto = Producto(codigoProducto, nombreProducto, descripcionProducto, precioUnitario)
    productos.append(producto)
    print(productos)
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

def realizar_compra(compras):
    print("Menú Compra")
    print("1. Agregar producto")
    print("2. Terminar compra y facturar")
    seleccion_compra = input("Ingrese la acción a realizar: ")
    if seleccion_compra == "1":
        print("Clientes registrados: ")
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. Nombre: {cliente.nombreCliente}, Correo: {cliente.correo}, NIT: {cliente.nit}")

        nit_cliente = input("Ingrese el NIT del cliente: ")
        cliente_seleccionado = next((cliente for cliente in clientes if str(cliente.nit) == nit_cliente), None)
        if cliente_seleccionado is None:
            print("Error: El NIT ingresado no corresponde a ningún cliente registrado.")
            return realizar_compra(compras)

        print("Productos disponibles:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Código: {producto.codigoProducto}, Nombre: {producto.nombreProducto}, Precio: {producto.precioUnitario}")

        productos_a_comprar = []
        while True:
            seleccion_producto = input("Ingrese el código de producto a comprar ('0' para terminar): ")
            if seleccion_producto == '0':
                break
            producto_seleccionado = next((producto for producto in productos if producto.codigoProducto == seleccion_producto), None)
            if producto_seleccionado:
                productos_a_comprar.append(producto_seleccionado)
            else:
                print("Código de producto no válido.")

        costo_total = sum(producto.precioUnitario for producto in productos_a_comprar)
        compra = Compra(productos_a_comprar, cliente_seleccionado, costo_total)
        compras.append(compra)
        print("Producto(s) agregado(s) a la compra.")
        print(compras)
        realizar_compra(compras)

    elif seleccion_compra == "2":
        if not clientes:
            print("Error: No hay clientes registrados.")
            return main()

        if not productos:
            print("Error: No hay productos registrados.")
            return main()

        print("Clientes registrados: ")
        for cliente in clientes:
            print(f"Nombre: {cliente.nombreCliente}, Correo: {cliente.correo}, NIT: {cliente.nit}")

        nit_cliente = input("Ingrese el NIT del cliente: ")
        cliente_seleccionado = next((cliente for cliente in clientes if str(cliente.nit) == nit_cliente), None)
        if cliente_seleccionado is None:
            print("Error: El NIT ingresado no corresponde a ningún cliente registrado.")
            return

        print("Supermercado Uolmart")
        print(f"Factura No.: {compras[-1].id_compra}")
        print("----------------------------")
        print("\nDatos del cliente")
        print(f"Nombre: {cliente_seleccionado.nombreCliente}")
        print(f"Correo electrónico: {cliente_seleccionado.correo}")
        print(f"NIT: {cliente_seleccionado.nit}")

        print("Productos comprados")
        for compra in compras:
            if compra.cliente == cliente_seleccionado:
                for producto in compra.productos:
                    print(f"Producto {producto.codigoProducto}: {producto.nombreProducto}, Q{producto.precioUnitario}")

        costo_total = sum(compra.costo_total for compra in compras if compra.cliente == cliente_seleccionado)
        impuesto = costo_total * 0.12
        costo_total_con_impuesto = costo_total + impuesto

        print("\nResumen")
        print(f"Subtotal: Q{costo_total}")
        print(f"Impuesto (12%): Q{impuesto}")
        print(f"Costo Total: Q{costo_total_con_impuesto}")
        facturas.append(compra)
        print(facturas)
        input()
        main()
    else:
        print("Opción inválida, intente nuevamente")

def realizar_reporte():
    print("Reporte de Compra")
    id_factura = input("Ingrese el ID de la factura: ")

    factura_encontrada = None
    for factura in facturas:
        if str(factura.id_compra) == id_factura:
            factura_encontrada = factura
            break

    if factura_encontrada is None:
        print("No se encontró ninguna factura con el ID ingresado.")
        return

    print("Factura:")
    print("----------")
    print(f"ID de Compra: {factura_encontrada.id_compra}")
    print("\nCliente")
    print(f"Nombre: {factura_encontrada.cliente.nombreCliente}")
    print(f"Correo eléctronico: {factura_encontrada.cliente.correo}")
    print(f"NIT: {factura_encontrada.cliente.nit}")
    print("Productos comprados")
    for producto in factura_encontrada.productos:
        print(f"Producto {producto.codigoProducto}: {producto.nombreProducto}, Q{producto.precioUnitario}")
    print("\nResumen")
    print(f"Costo Total: Q{factura_encontrada.costo_total}")
    print(f"Impuesto (12%): Q{factura_encontrada.impuesto}")
    print(f"Costo Total con Impuesto: Q{factura_encontrada.costo_total + factura_encontrada.impuesto}")
    print("--------------------------------------------")
    input()
    print("Opciones a realizar")
    print("1. Generar otro reporte")
    print("2. Regresar al menú principal")
    print("3. Salir")
    respuesta_reporte = input("Ingrese la opción que desea realizar: ")

    if respuesta_reporte == "1":
        realizar_reporte()
    elif respuesta_reporte == "2":
        main()
    elif respuesta_reporte == "3":
        print("¡Hasta luego!")
    else:
        print("Opción inválida, intente de nuevo")
main()



