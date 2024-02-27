class Cliente:
    def __init__(self, nombreCliente, correo, nit):
        self.nombreCliente = nombreCliente
        self.correo = correo
        self.nit = nit
        self.compras = []

    def agregar_compra(self, compra):
        self.compras.append(compra)
