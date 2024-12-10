
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Prueba básica de Streamlit con GitHub")

# Datos ficticios
data = {
    "Destinatario": ["Destinatario 1", "Destinatario 2", "Destinatario 3", "Destinatario 4", "Destinatario 5"],
    "Cartas Pendientes": [5, 8, 2, 4, 7],
    "Cartas Enviadas": [10, 5, 7, 3, 6],
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar tabla
st.header("Tabla de datos")
st.table(df)

# Gráfico de barras
st.header("Gráfico de barras: Cartas por destinatario")
fig, ax = plt.subplots()
df.plot(x="Destinatario", kind="bar", ax=ax)
st.pyplot(fig)

# Estadísticas básicas
st.header("Estadísticas")
st.write(f"Total de Cartas Pendientes: {df['Cartas Pendientes'].sum()}")
st.write(f"Total de Cartas Enviadas: {df['Cartas Enviadas'].sum()}")
