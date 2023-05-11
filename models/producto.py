class Producto:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def mostrar(self):
        print("Mi producto: ", self.id, self.nombre, self.descripcion, self.precio)
