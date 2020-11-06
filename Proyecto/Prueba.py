import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
plt.style.use("seaborn-dark")

def ReadCSV():
    data = pd.read_csv("A01022382_BasedeDatos.csv")
    #print(data)
    return data

def Regression(data, y, x1):
    x = sm.add_constant(x1)
    results = sm.OLS(y,x).fit()
    print(results.summary())  

def Graph(data, y, x1):
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # Color del fondo, toda la figura
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = 'white'  # Color de las etiquetas y números de los ejes

    fig, ax = plt.subplots()
    colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41',  # matrix green
    ]

    df1 = pd.DataFrame({'Carbs': x1['Carbohidratos (g)']})
    df2 = pd.DataFrame({'Fat': x1['Lípidos (g)']})
    df3 = pd.DataFrame({'Protein': x1['Proteína (g)']})

    df1.plot(marker='o', color='#08F7FE', ax=ax)  #Aqui podemos cambiar el color de las línea y marcadores
    df2.plot(marker='o', color='#FE53BB', ax=ax)  #Aqui podemos cambiar el color de las línea y marcadores
    df3.plot(marker='o', color='#00ff41', ax=ax)  #Aqui podemos cambiar el color de las línea y marcadores
    
    n_shades = 5
    diff_linewidth = 1.05
    alpha_value = 0.3 / n_shades
    for n in range(1, n_shades+1):
        df1.plot(marker='o',
                linewidth=2+(diff_linewidth*n),
                alpha=alpha_value,
                legend=False,
                ax=ax,
                color='#08F7FE')
        df2.plot(marker='o',
                linewidth=2+(diff_linewidth*n),
                alpha=alpha_value,
                legend=False,
                ax=ax,
                color='#FE53BB')
        df3.plot(marker='o',
                linewidth=2+(diff_linewidth*n),
                alpha=alpha_value,
                legend=False,
                ax=ax,
                color='#00ff41')
     
    for column, color in zip(df1, colors):
        ax.fill_between(x=df1.index,
                        y1=df1[column].values,
                        y2=[0] * len(df1),
                        color='#08F7FE',
                        alpha=0.1)
    
    for column, color in zip(df2, colors):
        ax.fill_between(x=df2.index,
                        y1=df2[column].values,
                        y2=[0] * len(df2),
                        color='#FE53BB',
                        alpha=0.1)
    
    for column, color in zip(df3, colors):
        ax.fill_between(x=df3.index,
                        y1=df3[column].values,
                        y2=[0] * len(df3),
                        color='#00ff41',
                        alpha=0.1)
    
    ax.grid(color='#F5D300', alpha = 0.3)  # Cambiar el grid
    font = {'fontname' : 'AppleMyungjo'} # Cambiar el tipo de fuente
    for tick in ax.get_xticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje X
    for tick in ax.get_yticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje Y
    
    plt.ylim(0, 400)
    plt.xticks(range(-5, 81, 10), size = 10)
    plt.yticks(size = 10)
    plt.title('Food', size = 30, fontstyle='oblique', **font)
    plt.ylabel("Grams", size = 20, fontstyle ='oblique', **font)
    plt.xlabel("Day", size = 20, fontstyle='oblique', **font)
    plt.show()


def GraphCals(y):
    df = y
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # Color del fondo, toda la figura
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = 'white'  # Color de las etiquetas y números de los ejes
    fig, ax = plt.subplots()
    colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41',  # matrix green
    ]

    df.plot(marker='o', color='#08F7FE', ax=ax)  #Aqui podemos cambiar el color de las línea y marcadores
    n_shades = 5
    diff_linewidth = 1.05
    alpha_value = 0.3 / n_shades
    for n in range(1, n_shades+1):
        df.plot(marker='o',
                linewidth=2+(diff_linewidth*n),
                alpha=alpha_value,
                legend=False,
                ax=ax,
                color='#08F7FE')
    
    
    
    ax.grid(color='#F5D300', alpha = 0.3)  # Cambiar el grid
    font = {'fontname' : 'AppleMyungjo'} # Cambiar el tipo de fuente
    for tick in ax.get_xticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje X
    for tick in ax.get_yticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje Y
    
    plt.ylabel("Calories", size = 20, fontstyle ='oblique', **font)
    plt.xlabel("Day", size = 20, fontstyle='oblique', **font)
    plt.show()

def main():
    data = ReadCSV()
    y = data['Calorias (kcal)']
    x1 = data[['Carbohidratos (g)',  'Lípidos (g)',  'Proteína (g)']]
    Regression(data, y, x1)
    Graph(data, y, x1)
    GraphCals(y)

    

main()