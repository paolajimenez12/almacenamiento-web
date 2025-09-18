import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

from utils import load_example_data, simulate_expansion, calculate_metrics

st.set_page_config(page_title="Storage Analysis", layout="wide")

st.title("📦 Storage Analysis Tool")
st.write("Sube tus datos de almacenamiento o usa el ejemplo para analizar, simular y exportar resultados.")

# --- Data input
option = st.radio("¿Cómo quieres cargar tus datos?", ["Ejemplo", "Subir CSV"])

if option == "Ejemplo":
    df = load_example_data()
elif option == "Subir CSV":
    uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()

st.subheader("Datos cargados")
st.dataframe(df)

# --- Metrics
metrics = calculate_metrics(df)
st.subheader("📊 Métricas básicas")
col1, col2, col3 = st.columns(3)
col1.metric("Total (GB)", f"{metrics['total']:.2f}")
col2.metric("Promedio (GB)", f"{metrics['mean']:.2f}")
col3.metric("Máximo (GB)", f"{metrics['max']:.2f}")

# --- Simulation
st.subheader("🔮 Simulación de crecimiento")
growth = st.slider("Crecimiento anual (%)", 0, 100, 20)
years = st.slider("Años a simular", 1, 10, 5)

simulated = simulate_expansion(df, growth, years)
st.line_chart(simulated.set_index("Año")["Capacidad proyectada"])

# --- Export
st.subheader("📥 Exportar resultados")
output = io.BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    simulated.to_excel(writer, sheet_name="Simulación", index=False)

st.download_button(
    label="Descargar resultados en Excel",
    data=output.getvalue(),
    file_name="storage_analysis.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
