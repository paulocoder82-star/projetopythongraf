import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
# 1. Carregar o arquivo
# Como a imagem mostra que a primeira coluna não tem título, 
# vamos carregá-lo e o Pandas automaticamente usará a primeira coluna como índice.
df = pd.read_csv('wine.csv', encoding='utf-8')
# 2. Dar um nome para a primeira coluna que está "anônima"
df.index.name = 'Classe'
df_visual = df.reset_index().head(10)
# 3. Exibir a tabela no terminal (exatamente como na sua foto)
fig = ff.create_table(df_visual) 

fig.show()