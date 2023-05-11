import streamlit as st

class Inventario:
    def __init__(self):
        if "productos" in st.session_state:
            self.productos = st.session_state["productos"]
        else:
            self.productos = []
            st.session_state["productos"] = []

    def crear_producto(self, producto):
        self.productos.append(producto)
        st.session_state["productos"] = self.productos

    def actualizar_producto(self, id, nombre = None, descripcion = None, precio = None):
        for producto in self.productos:
            if producto.id == id:
                if nombre:
                    producto.nombre = nombre
                if descripcion:
                    producto.descripcion = descripcion
                if precio:
                    producto.precio = precio

    def borrar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                self.productos.pop(i)
                st.session_state["productos"] = self.productos
                return True
        return False
