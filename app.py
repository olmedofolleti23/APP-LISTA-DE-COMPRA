import streamlit as st

# Configuración de la página para que parezca una app
st.set_page_config(page_title="Lista de Mamá", page_icon="🛒")

# Título grande
st.title("🛒 Lista de la Compra")

# Inicializar la lista en la memoria si no existe
if 'lista_compra' not in st.session_state:
    st.session_state.lista_compra = []

# --- ZONA DE AÑADIR ---
st.header("¿Qué necesitas comprar?")


def agregar_item():
    item = st.session_state.nuevo_item
    if item:
        st.session_state.lista_compra.append({"nombre": item, "hecho": False})
        st.session_state.nuevo_item = ""  # Limpiar el campo


# Campo de texto y botón
st.text_input("Escribe aquí el producto", key="nuevo_item", on_change=agregar_item)
if st.button("Añadir a la lista", use_container_width=True):
    pass  # La lógica ya está en on_change, pero el botón ayuda visualmente

st.divider()

# --- ZONA DE LISTA ---
st.header("Pendiente:")

if not st.session_state.lista_compra:
    st.info("La lista está vacía. ¡Añade algo arriba!")
else:
    # Mostramos la lista con casillas
    items_a_borrar = []

    for i, producto in enumerate(st.session_state.lista_compra):
        # Checkbox para marcar como comprado
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            check = st.checkbox("", key=f"check_{i}")
        with col2:
            if check:
                st.markdown(f"~~{producto['nombre']}~~")  # Tachado visual
                items_a_borrar.append(i)
            else:
                st.markdown(f"**{producto['nombre']}**")

    # Botón para limpiar lo completado
    if items_a_borrar:
        st.write("")  # Espacio
        if st.button("🗑️ Borrar productos marcados", type="primary", use_container_width=True):
            # Reconstruimos la lista solo con lo NO marcado
            st.session_state.lista_compra = [
                p for i, p in enumerate(st.session_state.lista_compra)
                if i not in items_a_borrar
            ]
            st.rerun()  # Recargar la página

# --- PIE DE PÁGINA ---
st.divider()
if st.button("Borrar TODA la lista (Reiniciar)"):
    st.session_state.lista_compra = []
    st.rerun()