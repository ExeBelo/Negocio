class Producto:
    def __init__(self, nombre, precio, stock_actual):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_actual  

    def comprobar_stock(self, cantidad):
        if cantidad <= self.stock:
            return True
        else:
            return False


