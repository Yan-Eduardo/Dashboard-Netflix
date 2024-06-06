# Importação das dependências
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define as configurações da página
st.set_page_config(
    page_title="Netflix",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Importando o css
with open("style.css") as fp:
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

## Lendo o .csv e criando um dataframe a partir dele
df = pd.read_csv("dataset.csv", sep=",")

# Alterações na base de dados
df["Date"] = pd.to_datetime(df["Join Date"], format="%d-%m-%y") # Converte a coluna "Date" para o formato datetime e especifica o formato de data utilizado no csv.
df = df.sort_values("Date") # Ordena o DataFrame por data
df["Year"] = df["Date"].apply(lambda x: str(x.year)) # Coluna "Year" com base no ano

#######################
# Barra lateral
with st.sidebar:
    st.title('Assinaturas Netflix📈')
    unique_years = df["Year"].unique()
    selected_years = st.multiselect(
        'Anos', unique_years, default=unique_years[:3]) #permite ao usuário selecionas os anos que deseja visualizar
    df_filtered = df[df["Year"].isin(selected_years)]
    unique_plans = df["Subscription Type"].unique()
    selected_plans = st.multiselect(
        'Planos', unique_plans, default=unique_plans[:]) #Permite ao usuário selecionar os planos que deseja visualizar
    df_filtered = df_filtered[df_filtered["Subscription Type"].isin(selected_plans)]
    st.markdown("Aluno: Yan Eduardo Carneiro Cruz\nPDITA:075") #Exibe o nome do aluno e o número da matrícula

#######################
# criando fórmula para calular renda total
revenue = df_filtered["User ID"].count()
revenue_count = (revenue*15)
# primeira linha: métricas
col1= st.columns(2)
col1[0].metric('Faturamento total', f'${revenue_count:,.2f}')
col1[1].metric('Número de assinantes', f'{df_filtered["User ID"].count()}')

#######################
# Segunda linha: choropleth e pie
# Criando o choropleth
choropleth = px.choropleth(df_filtered,
                        locations="Country",
                        color="User ID",
                        scope="world",
                        labels={"Country":"País",
                                "User ID":"Assinantes"},
                        color_continuous_scale=["#c1071e","#dedede","#43465e","#131834"])
#######################
# Criando o pie
pie = px.pie(
    data_frame=df_filtered,
    values="User ID",
    names="Device",
    labels={
        "Device":"Dispositivo",
        "User ID":"Assinantes"},
    color_discrete_sequence=["#c1071e","#dedede","#43465e","#131834"],
    width=500,
    height=300)
#Criando a coluna e adicionando o choropleth e pie à mesma
col2 = st.columns([2, 1])
with col2[0]:
    st.title("Número de assinantes")
    st.plotly_chart(choropleth, use_container_width=False)
with col2[1]:
    st.title("Plataformas utilizadas")
    st.plotly_chart(pie, use_container_width=False)