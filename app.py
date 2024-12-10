import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de datos iniciales
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=[
        'Nombre de la Carta', 'Destinatario', 'Fecha de Notificación', 
        'Hora', 'Estado', 'Asunto', 'Carta de Respuesta', 'Fecha de Respuesta', 
        'Días de Respuesta', 'Fecha Límite'
    ])

# Función para calcular la fecha límite
def calcular_fecha_limite(fecha_respuesta, dias):
    if pd.notna(fecha_respuesta) and dias:
        return pd.to_datetime(fecha_respuesta) + pd.to_timedelta(dias, unit='d')
    return None

# Sección 1: Actualizar carta
def actualizar_carta():
    st.header("Actualizar Carta")
    nombre_carta = st.selectbox("Seleccione una carta", st.session_state['data']['Nombre de la Carta'].unique())
    carta_data = st.session_state['data'][st.session_state['data']['Nombre de la Carta'] == nombre_carta]

    if not carta_data.empty:
        estado = st.selectbox("Estado", ["Pendiente", "Resuelta", "En Proceso"], index=0)
        carta_respuesta = st.text_input("Carta de Respuesta", carta_data.iloc[0]['Carta de Respuesta'])
        codigo_mvp = st.text_input("Código MVP", "")
        fecha_respuesta = st.date_input("Fecha de Respuesta", pd.to_datetime(carta_data.iloc[0]['Fecha de Respuesta']))
        dias_respuesta = st.number_input("Días de Respuesta", min_value=0, value=0)
        fecha_limite = calcular_fecha_limite(fecha_respuesta, dias_respuesta)
        
        if st.button("Actualizar"):
            st.session_state['data'].loc[
                st.session_state['data']['Nombre de la Carta'] == nombre_carta,
                ['Estado', 'Carta de Respuesta', 'Fecha de Respuesta', 'Días de Respuesta', 'Fecha Límite']
            ] = estado, carta_respuesta, fecha_respuesta, dias_respuesta, fecha_limite
            st.success("Carta actualizada correctamente.")

# Sección 2: Agregar nueva carta
def agregar_nueva_carta():
    st.header("Agregar Nueva Carta")
    nombre_carta = st.text_input("Nombre de la Carta")
    destinatario = st.text_input("Destinatario")
    fecha_notificacion = st.date_input("Fecha de Notificación")
    hora = st.time_input("Hora")
    estado = st.selectbox("Estado", ["Pendiente", "Resuelta", "En Proceso"], index=0)
    asunto = st.text_input("Asunto")
    
    if st.button("Agregar"):
        nueva_carta = {
            'Nombre de la Carta': nombre_carta,
            'Destinatario': destinatario,
            'Fecha de Notificación': fecha_notificacion,
            'Hora': hora,
            'Estado': estado,
            'Asunto': asunto,
            'Carta de Respuesta': None,
            'Fecha de Respuesta': None,
            'Días de Respuesta': None,
            'Fecha Límite': None
        }
        st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([nueva_carta])], ignore_index=True)
        st.success("Carta agregada correctamente.")

# Sección 3: Gráfica y estadísticas
def graficas_y_estadisticas():
    st.header("Gráfica y Estadísticas")
    data = st.session_state['data']
    
    # Gráfica por estado
    fig1, ax1 = plt.subplots()
    data['Estado'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title('Cartas por Estado')
    st.pyplot(fig1)

    # Gráfica por destinatario
    fig2, ax2 = plt.subplots()
    data['Destinatario'].value_counts().plot(kind='bar', ax=ax2)
    ax2.set_title('Cartas por Destinatario')
    st.pyplot(fig2)

    # Estadísticas generales
    st.subheader("Estadísticas Generales")
    st.write("Total de Cartas Registradas:", len(data))
    st.write("Estados:", data['Estado'].value_counts())

# Navegación
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Selecciona una sección", ["Actualizar Carta", "Agregar Nueva Carta", "Gráfica y Estadísticas"])

if seccion == "Actualizar Carta":
    actualizar_carta()
elif seccion == "Agregar Nueva Carta":
    agregar_nueva_carta()
elif seccion == "Gráfica y Estadísticas":
    graficas_y_estadisticas()

