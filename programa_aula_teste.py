# Bibliotecas
import streamlit as st
import pandas as pd  
import matplotlib.pyplot as plt


# Título na barra do navegador
st.set_page_config(

page_title="Teste de Site",
page_icon="📈", 
)


# Cabeçalho
st.header("📌Dados da Empresa 1")

arquivo = "https://raw.githubusercontent.com/PaolaRamina/aula_teste/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))

"---"
# Cabeçalho
st.subheader("📊Gráficos comparando Dados")
st.write("**Indicadores ao longo do Tempo**")
fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)

st.write("**Dispersão entre EBITDA e o Lucro Operacional**")
fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)

st.write("**Histograma do Lucro do Período**")
fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)

"---"
# Cabeçalho
st.subheader("📍Soma dos Valores de cada Ano")
st.write(dfe.groupby('Ano').mean())


"..."
nome1 = input("Insira o nome da primeira pessoa>")
idade1 = input("Quantos anos essa pessoa tem?")
nome2 = input("Insira o nome da segunda pessoa>")
idade2 = input("Quantos anos essa pessoa tem?")

if idade1 > idade2:
  st.write(nome1, "é mais velho(a) que", nome2)

elif idade1 < idade2:
  st.write(nome2, "é mais velho(a) que", nome1)

else:
  st.write(nome1, "e", nome2, "possuem a mesma idade")


    
