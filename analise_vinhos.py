import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
# Certifique-se que o arquivo wine.csv está na mesma pasta do código
df = pd.read_csv('wine.csv')

# 2. Configuração estética do gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Criar a visualização
# Vamos observar a relação entre Álcool e Intensidade de Cor
grafico = sns.scatterplot(
    data=df, 
    x='Alcohol', 
    y='Color_intensity', 
    hue='Alcohol', # Ou use a coluna de classificação se houver
    palette='flare',
    size='Magnesium', # O tamanho do ponto indica o Magnésio
    sizes=(20, 200)
)

# 4. Personalização
plt.title('Análise Química dos Vinhos: Álcool vs Intensidade de Cor', fontsize=15)
plt.xlabel('Teor Alcoólico', fontsize=12)
plt.ylabel('Intensidade da Cor', fontsize=12)

# Exibir o gráfico
plt.show()