import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_csv('wine.csv')

# --- CORREÇÃO DO ERRO ---
# Remove espaços em branco que podem estar escondidos nos nomes das colunas
df.columns = df.columns.str.strip()

# Se a primeira coluna virou 'index' ou não tem nome, vamos dar um nome a ela
# No seu caso, a primeira coluna é a 'Classe' do vinho
df = df.reset_index()
df.rename(columns={df.columns[0]: 'Classe_Vinho', 'index': 'Classe_Vinho'}, inplace=True)

# Vamos imprimir os nomes reais das colunas para você conferir no terminal
print("Colunas detectadas:", df.columns.tolist())

# 2. Criar o gráfico
plt.figure(figsize=(10, 6))

# Usando o nome da coluna que limpamos acima
sns.barplot(data=df, x='Classe_Vinho', y='Alcohol', hue='Classe_Vinho', palette='viridis', legend=False)

# 3. Personalizar
plt.title('Média de Álcool por Classe de Vinho', fontsize=14)
plt.xlabel('Classe do Vinho (Segmento)', fontsize=12)
plt.ylabel('Teor Alcoólico', fontsize=12)

# 4. SALVAR O GRÁFICO (para você baixar)
plt.savefig('grafico_vinhos_final.png', dpi=300, bbox_inches='tight')
print("Sucesso! O arquivo 'grafico_vinhos_final.png' foi criado na sua pasta.")

plt.show()