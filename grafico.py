import streamlit as st
import pandas as pd

dados = pd.read_csv('Joao.csv.csv')
st.write(dados.head(10))

st.title('Publicações mais curtidas')
st.write(dados)

chart_data = dados[['Link', 'Likes']]
st.bar_chart(chart_data.set_index('Link'))
