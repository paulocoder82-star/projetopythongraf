import pandas as pd
import plotly.express as px    

dados_vinho = pd.read_csv('wine.csv', encoding='utf-8')

vis = px.parallel_coordinates(dados_vinho, color='Color_intensity',
    dimensions=['Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_ash', 'Flavanoids', 'Nonflavanoid_phenols'],
    labels={
        'Alcohol': 'Álcool',
        'Malic_acid': 'Ácido Málico',
        'Ash': 'Cinzas',
        'Alcalinity_ash': 'Alcalinidade',
        'Flavanoids': 'Flavonoides',
        'Nonflavanoid_phenols': 'Fenóis Não Flavonoides'},color_continuous_scale= px.colors.sequential.Viridis, range_color=[2,10])
vis.show()


