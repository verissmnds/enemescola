import pandas as pd
import streamlit as st 
import numpy as np
st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)

chart_data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=[x='pessoa', y='salario'])

st.bar_chart(chart_data)
