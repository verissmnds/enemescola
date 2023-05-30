import pandas as pd
import streamlit as st 
import numpy as np

st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)

st.bar_chart(data=dados, x=pessoa, y=salario, *, width=10, height=15, use_container_width=True)
