import streamlit as st
import pandas as pd
import numpy as np

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)

st.title('Empresa Cariocas')

st.write("Tabela")

dataframe = pd.DataFrame(dados)

dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['pessoa','salario'])

st.bar_chart(chart_data)
