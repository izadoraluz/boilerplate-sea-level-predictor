import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leia os dados
    df = pd.read_csv('epa-sea-level.csv')

    # Criar a figura e o eixo
    fig, ax = plt.subplots(figsize=(10, 6))

    # Criar o gráfico de dispersão
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Linha de melhor ajuste para todos os dados
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_predicted = slope * years_extended + intercept
    ax.plot(years_extended, sea_level_predicted, color='red', label='Fit: All Data')

    # Linha de melhor ajuste desde o ano 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_level_recent_predicted = slope_recent * years_recent_extended + intercept_recent
    ax.plot(years_recent_extended, sea_level_recent_predicted, color='green', label='Fit: From 2000')

    # Configurações do gráfico
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    ax.grid(True)

    # Salvar o gráfico
    plt.savefig('sea_level_plot.png')
    return ax
