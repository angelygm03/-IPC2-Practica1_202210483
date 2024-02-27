class Compra:
    contador_facturas = 0
    def __init__(self, productos, cliente, costo_total):
        Compra.contador_facturas += 1
        self.id_compra = Compra.contador_facturas
        self.productos = productos
        self.cliente = cliente
        self.costo_total = costo_total
        self.impuesto = costo_total * 0.12