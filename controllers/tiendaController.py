import streamlit as st
import time


class TiendaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            try:
                producto = self.vista.menu_crear_producto()
                if producto:
                    self.modelo.crear_producto(producto)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presentó un error creando el producto")
        if opcion == 2:
            self.vista.listar_productos(self.modelo.productos)
        if opcion == 3:
            self.vista.menu_actualizar_producto(self.modelo.productos)
        if opcion == 4:
            resultado = self.modelo.borrar_producto(self.vista.menu_borrar_producto(self.modelo.productos))
            if resultado:
                self.vista.mostrar_mensaje_exitoso("El producto fue eliminado correctamente")
                # Primero mostramos el mensaje y esperamos 2 segundos para forzar la actualización de la vista
                time.sleep(2)
                st.experimental_rerun()

    def aplicar_formato_tabla(self, productos):
        datos = []
        for producto in productos:
            datos.append([producto.id, producto.nombre, producto.descripcion, producto.precio])
        return datos