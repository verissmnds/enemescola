import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt

pip install matplotlib==3.4.3

st.title('Gráfico de Salários')

dados = pd.read_csv('grafico.csv')

df = pd.DataFrame(dados)

fig, ax = plt.subplots()
ax.barh(df['pessoa'], df['salario'], color='g')
ax.set_xlabel('salario')
ax.set_ylabel('pessoa')
ax.set_title('Empresa Farm')

st.pyplot(fig)
