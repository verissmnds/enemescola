import streamlit as st
import pandas as pd

dados = pd.read_csv('Joao.csv.csv')

st.title('Publicações mais curtidas do Instagram de João Campos')

st.bar_chart(dados, x = 'pessoa', y = 'salario')

chart_data = dados[['Link', 'Likes']].sort_values(by='Likes', ascending=False).head(10)
st.bar_chart(chart_data.set_index('Link'))

st.title('Se quiser, acesse as publicações e confira!')
for index, row in chart_data.iterrows():
    link = row['Link']
    likes = row['Likes']
    st.markdown(f'- [{link}]({link}) - Likes: {likes}')
