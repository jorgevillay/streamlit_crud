import views.tienda as tiendaView
import streamlit as st


if __name__ == '__main__':
    st.set_page_config(
        page_title="CRUD de una tienda",
        layout="wide"
    )
    tienda = tiendaView.Tienda()
    tienda.mostrar_menu()
