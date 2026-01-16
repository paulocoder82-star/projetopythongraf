import pandas as pd
import plotly.express as px

# 1. Carregar os dados
# index_col=0 diz ao Pandas para usar a primeira coluna (as classes) como identificador
dados_vinho = pd.read_csv('wine.csv', encoding='utf-8', index_col=0)

# 2. Como a coluna de classe não tem nome na imagem, vamos dar um nome a ela agora
dados_vinho.index.name = 'Classe_Vinho'

# 3. Resetar o índice para que 'Classe_Vinho' vire uma coluna normal que o Plotly consiga ler
dados_vinho = dados_vinho.reset_index()

print("Colunas prontas para o gráfico:", dados_vinho.columns.tolist())

# 4. Criar o gráfico
vis2 = px.scatter(dados_vinho, 
                 x="Malic_acid", 
                 y="Alcohol", 
                 color="Color_intensity",
                 size="Flavanoids",
                 color_continuous_scale=px.colors.sequential.Viridis,
                 range_color=[2, 10],
                 labels={"Color_intensity": "Intensidade da Cor", "Alcohol": "Teor Alcoólico", "Malic_acid": "Ácido Málico", "Flavanoids": "Flavonoides"},)

# 5. Exibir o gráfico
vis2.show()