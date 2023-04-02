import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    # Gerando 100 dias de dados fictícios da bolsa de valores
    days = np.arange(1, 101)
    # Gerando preços fictícios com uma média de 100 e desvio padrão de 10
    prices = np.random.normal(100, 10, size=100)
    # Gerando variações diárias fictícias com uma média de 0 e desvio padrão de 1
    daily_changes = np.random.normal(0, 1, size=100)
    # Calculando os preços de fechamento fictícios
    close_prices = prices + daily_changes
    # Retornando um DataFrame com os dados gerados
    return pd.DataFrame({'Dia': days, 'Preço': prices, 'Variação Diária': daily_changes, 'Fechamento': close_prices})


def main():
    # Configurando o título do aplicativo
    st.title('Dados da Bolsa de Valores')
    
    # Gerando os dados fictícios da bolsa de valores
    data = generate_data()
    
    # Exibindo os dados em um gráfico de linha
    st.line_chart(data['Fechamento'])
    
    # Exibindo os dados em uma tabela
    st.write(data)
    
    
def generate_currency_data():
    # Gerando os dados fictícios de cotações de moedas
    currency_data = pd.DataFrame({
        'Moeda': ['USD', 'EUR', 'JPY', 'GBP'],
        'Cotação Atual': np.random.normal([5, 6, 1, 8], [0.5, 0.7, 0.1, 1], size=4),
        'Maior Valor': np.random.normal([5.5, 6.5, 1.2, 8.5], [0.5, 0.7, 0.1, 1], size=4),
        'Menor Valor': np.random.normal([4.5, 5.5, 0.8, 7.5], [0.5, 0.7, 0.1, 1], size=4),
        'Variação Diária': np.random.normal([0.01, -0.005, 0.002, -0.008], [0.002, 0.003, 0.001, 0.004], size=4)
    })
    return currency_data
# Gerando os dados fictícios de cotações de moedas
currency_data = generate_currency_data()

# Exibindo os cards com as informações de cotação de cada moeda
# Exibindo os cards com as informações de cotação de cada moeda
st.subheader('Cotações de Moedas')
col1, col2, col3, col4 = st.beta_columns(4)
for index, row in currency_data.iterrows():
    with col1:
        st.write(row['Moeda'])
    with col2:
        st.write('Cotação Atual:')
        st.write(row['Cotação Atual'])
    with col3:
        st.write('Variação Diária:')
        st.write(row['Variação Diária'])
    with col4:
        st.write('Maior/Menor Valor:')
        st.write(f"{row['Menor Valor']} - {row['Maior Valor']}")


# Adicionando uma barra lateral com filtros
st.sidebar.title('Filtros')
# Adicionando um slider para selecionar o número de dias
num_days = st.sidebar.slider('Número de Dias', 10, 100, 30)

# Gerando um gráfico de projeção
projection_days = np.arange(101, 151)
projection_prices = np.random.normal(100, 10, size=50)
for i in range(1, 50):
    projection_prices[i] = projection_prices[i-1] + np.random.normal(0, 1)
projection_data = pd.DataFrame({'Dia': projection_days, 'Projeção': projection_prices})
projection_data['Dia'] = projection_data['Dia']

# Gerando mais dois gráficos para o dashboard
st.subheader('Gráficos')
col1, col2 = st.beta_columns(2)
with col1:
    st.line_chart(projection_data.set_index('Dia')['Projeção'])
with col2:
    st.bar_chart(currency_data.set_index('Moeda')['Cotação Atual'])
    
    # Exibindo os cards com as informações de cotação de cada moeda
st.subheader('Cotações de Moedas')
col1, col2, col3, col4 = st.beta_columns(4)
for index, row in currency_data.iterrows():
    with col1:
        st.write(row['Moeda'])
        st.write(f"Cotação Atual: {row['Cotação Atual']}")
    with col2:
        st.write("")
        st.write(f"Variação Diária: {row['Variação Diária']}")
    with col3:
        st.write("")
        st.write(f"Maior/Menor Valor: {row['Menor Valor']} - {row['Maior Valor']}")
    with col4:
        st.write("")


    
    
    
if __name__ == '__main__':
    main()
