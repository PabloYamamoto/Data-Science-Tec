import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-dark") # Añade un gris de fondo a la gráfica


def Graph(data):

    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # Color del fondo, toda la figura
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = 'white'  # Color de las etiquetas y números de los ejes

    colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41',  # matrix green
    ]

    df = data['SAT'] # Graficamos solo una variable de data, en este caso SAT (tenemos GPA tambien)
    
    fig, ax = plt.subplots()
    
    df.plot(marker='o', color='#08F7FE', ax=ax)  #Aqui podemos cambiar el color de las línea y marcadores

    # Esta parte del código nos da las sombras alrededor de las líneas graficadas, es un efecto sombra. 
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
     

    
    
    # Graficar los datos
    
    ax.grid(color='#F5D300', alpha = 0.3)  # Cambiar el grid
    font = {'fontname' : 'AppleMyungjo'} # Cambiar el tipo de fuente
    for tick in ax.get_xticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje X
    for tick in ax.get_yticklabels():
        tick.set_fontname('AppleMyungjo') # Cambiar el tipo de fuente del eje Y
    plt.xlabel("Number of student", **font)
    plt.ylabel("Score", **font)
    plt.title("SAT", size = 30, **font)
    plt.show()


def main():
    data = pd.read_csv('1.01. Simple linear regression.csv') # Leemos la información del CSV
    Graph(data)

main()