import pandas as pd
import streamlit as st 
import numpy as np
st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')

dados.style.highlight_max(axis=0)

st.write(dados)
chart_data = pd.DataFrame(
     np.random.randn(20, 3)
st.bar_chart(dados)
