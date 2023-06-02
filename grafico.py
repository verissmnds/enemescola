import pandas as pd
import streamlit as st 
import numpy as np
st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')

dados.style.highlight_max(axis=0)

st.write(dados['salario','pessoa'])

st.bar_chart(dados)
