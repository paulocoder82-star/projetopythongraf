import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.read_csv('wine.csv')

# 2. Calcular a matriz de correlação
# O método .corr() calcula a relação entre todas as colunas numéricas
corr = df.corr()

# 3. Configurar a visualização
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='RdBu_r', center=0, linewidths=.5)

# 4. Finalização
plt.title('Mapa de Calor: Correlação entre Atributos Químicos do Vinho', fontsize=16)
plt.savefig('correlation_heatmap.png') #salva o gráfico como imagem
plt.show()
