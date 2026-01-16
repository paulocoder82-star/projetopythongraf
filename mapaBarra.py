import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
# Se o seu arquivo não tiver cabeçalho na primeira coluna, o pandas pode se confundir.
# Mas baseando no seu arquivo, a primeira coluna parece ser o 'Customer_Segment' ou 'Type'
df = pd.read_csv('wine.csv')

# Vamos nomear a primeira coluna de 'Tipo' caso ela não tenha nome
df.rename(columns={df.columns[0]: 'Tipo_Vinho'}, inplace=True)

# 2. Criar o gráfico de barras (Média de Álcool por Tipo)
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Tipo_Vinho', y='Alcohol', estimator='mean', hue='Tipo_Vinho', legend=False)

# 3. Personalizar
plt.title('Média de Teor Alcoólico por Tipo de Vinho', fontsize=14)
plt.xlabel('Tipo de Vinho', fontsize=12)
plt.ylabel('Média de Álcool', fontsize=12)

# 4. Exibir
plt.savefig('mapaBarra.png', dpi=300, bbox_inches='tight')

print("Gráfico salvo com sucesso como 'meu_grafico_vinhos.png'!")

# 3. Mostrar na tela (opcional)
plt.show()

