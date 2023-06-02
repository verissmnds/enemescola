import streamlit as st
import pandas as pd

dados = pd.read_csv('Joao.csv.csv')

st.title('Publicações mais curtidas do Instagram de João Campos')

chart_data = dados[['Link', 'Likes']].sort_values(by='Likes', ascending=False).head(10)
st.bar_chart(chart_data.set_index('Link'))

st.title('Se quiser, acesse as publicações e confira!')
st.write(chart_data['Link'].to_frame().style.format(template='<a href="{link}" target="_blank">{link}</a>'))
