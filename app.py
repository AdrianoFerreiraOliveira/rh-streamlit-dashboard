import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações gerais
st.set_page_config(page_title='Dashboard de RH',  page_icon="chart_with_upwards_trend", layout='wide')

# Título da página
st.title('Dashboard de RH')

# Subtítulo e texto de introdução
st.markdown('Este dashboard apresenta informações fictícias de recursos humanos.')
st.markdown('As informações estão apresentadas em um mapa e um gráfico de linhas.')

# Sidebar com filtros
st.sidebar.title('Filtros')
departamentos = ['Administração', 'Financeiro', 'Marketing', 'RH', 'Tecnologia']
dept = st.sidebar.multiselect('Selecione o(s) departamento(s)', departamentos, default=departamentos)
idade_min = st.sidebar.slider('Idade mínima', min_value=18, max_value=65, value=18, step=1)
idade_max = st.sidebar.slider('Idade máxima', min_value=18, max_value=65, value=65, step=1)



# Carrega dados fictícios de RH
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Laura', 'Pedro', 'Luíza', 'Felipe', 'Mariana'],
    'Departamento': np.random.choice(departamentos, size=10),
    'Idade': np.random.randint(idade_min, idade_max+1, size=10),
    'Salário': np.random.normal(loc=5000, scale=1000, size=10),
    'País': ['Brazil', 'United States', 'France', 'Italy', 'Japan', 'Mexico', 'United Kingdom', 'Russia', 'Sweden', 'Switzerland']
})

# Filtra dados de acordo com os filtros da sidebar
df_filtrado = df[df['Departamento'].isin(dept) & (df['Idade'] >= idade_min) & (df['Idade'] <= idade_max)]

st.write("")
st.write("")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Ativos", "350", "1.2%")
col2.metric("Desligados", "50", "-15%")
col3.metric("Turnover Mensal", "10%", "4%")
col4.metric("Turnover Anual", "8%", "-4%")





# Gráfico de linhas com a evolução do salário médio por idade
st.header('Evolução do salário médio por idade')
salario_medio = df_filtrado.groupby('Idade')['Salário'].mean().reset_index()
fig_linhas = px.line(salario_medio, x='Idade', y='Salário', title='Evolução do salário médio por idade')
fig_linhas.update_layout(xaxis_title='Idade', yaxis_title='Salário médio')
st.plotly_chart(fig_linhas)

# Configurando o título e subtítulo da página
st.title('Distribuição de Salários')
st.write('Este é um exemplo de gráfico de colunas utilizando a biblioteca Matplotlib')

# Criando dados aleatórios de salários
salarios = np.random.normal(loc=5000, scale=1000, size=1000)

# Criando o gráfico de colunas
bin_edges = np.arange(0, 10000, 1000)
plt.hist(salarios, bins=bin_edges, rwidth=0.5, color='red')

# Configurando o título e os rótulos dos eixos
plt.title('Distribuição de Salários')
plt.xlabel('Salário (R$)')
plt.ylabel('Número de Funcionários')

# Exibindo o gráfico no Streamlit
fig, ax = plt.subplots()
ax.hist(salarios, bins=bin_edges, rwidth=0.5, color='black')
st.pyplot(fig)

import streamlit as st
import pandas as pd

# Dados fictícios de RH
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Bruna', 'Carlos', 'Débora', 'Eduardo', 'Fernanda'],
    'Cargo': ['Analista', 'Coordenador', 'Analista', 'Assistente', 'Estagiário', 'Analista', 'Assistente', 'Estagiário', 'Coordenador', 'Analista'],
    'Idade': [28, 34, 26, 23, 22, 31, 25, 24, 29, 27],
    'Salário': [4500, 6500, 3800, 2800, 1200, 4200, 2600, 1500, 7000, 5000],
    'Status': ['Ativo', 'Desligado', 'Ativo', 'Desligado', 'Ativo', 'Ativo', 'Desligado', 'Ativo', 'Ativo', 'Desligado']
})