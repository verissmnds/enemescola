import pandas as pd
import streamlit as st 
import numpy as np
st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')

df = pd.DataFrame(dados)

X = df['pessoa']
Y = df['salario']
  
plt.bar(X, Y, color='g')
plt.title("Empresa Farm")
plt.xlabel("pessoa")
plt.ylabel("salario")

st.pyplot(plt)
