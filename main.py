class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0
        self.descuento = 0

    def agregar_descuento(self, porcentaje):
        self.precio = self.precio * (1 - porcentaje / 100)


