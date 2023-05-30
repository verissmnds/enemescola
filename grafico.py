import pandas as pd
import streamlit as st 

st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')
st.dataframe(dados)

st.bar_chart(data=dados, x=pessoa, y=salario, width=0, height=0, use_container_width=True)
