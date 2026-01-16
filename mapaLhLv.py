import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt     
df = pd.read_csv('wine.csv')
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Alcohol', y='Color_intensity', hue='Alcohol', palette='viridis')

plt.title('Relação entre teor alcoólico e intensidade de cor', fontsize=15)
plt.xlabel('Teor Alcoólico', fontsize=12)
plt.ylabel('Intensidade da Cor', fontsize=12)
plt.show()


