class Compra:
    def __init__(self, productos, cliente, costo_total):
        self.id_compra = None 
        self.productos = productos
        self.cliente = cliente
        self.costo_total = costo_total
        self.impuesto = costo_total * 0.12
    
    def generar_reporte(self):
        print("---------------------------------------------")
        print("             Supermercado Uolmart")
        print("                 Factura No.", self.id_compra)
        print("---------------------------------------------\n")
        print("Datos del cliente")
        print("Nombre:", self.cliente.nombreCliente)
        print("Correo electrónico:", self.cliente.correo)
        print("NIT:", self.cliente.nit)
        print()
        print("Productos comprados")

        for producto in self.productos:
            print("Producto:", producto.nombreProducto, "Q" + str(producto.precioUnitario))

        print("\nResumen")
        print("Subtotal:", self.costo_total)
        print("Impuesto (12%):", round(self.costo_total * 0.12,2))
        print("Total a pagar:", round(self.costo_total * 1.12, 2))
        print("---------------------------------------------")
