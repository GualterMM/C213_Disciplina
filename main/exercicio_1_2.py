from scipy.io import loadmat
import matplotlib.pyplot as plt

# Exercício 1 - Levante a função de transferência da planta destinada ao seu grupo

# Importando os dados 
mat = loadmat('../TransferFunction5.mat')

# Extraindo as variáveis 'saída', 'degrau' e 't (tempo)'
degrau = mat.get('degrau')
saida = mat.get('saida')
t = mat.get('t')

# Plotando os gráficos
plt.plot(t.T,saida, label='Saída')
plt.plot(t.T,degrau,label='Degrau de entrada')

# Definindo as legendas e título do gráfico
plt.xlabel (' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Função de transferência fornecida ao grupo')
plt.legend(loc="upper left")

# Configurando opções de exibição do gráfico
plt.grid()
plt.show()

# Exercício 2 - Escolha o método de identificação da planta e com isso encontre os valores de k, Ɵ e τ

# Valores obtido pelo método de Smith
y_max = max(saida)                  # Valor máximo do sinal
d_Y = y_max - min(saida)            # Delta do sinal
d_u = 5                             # Valor do degrau unitário

# Obtendo o valor do sinal em 28,3% para determinar t1
y_t1 = y_max * 0.283                # y(t1) = 3.52
t1 = 5.98                           # Obtido por observação do gráfico

# Obtendo o valor do sinal em 63,2% para determinar t2
y_t2 = y_max * 0.632                # y(t2) = 7.86
t2 = 9.94                           # Obtido por observação do gráfico

# Obtendo valores de k, Ɵ e τ
k = d_Y/d_u                         # k = 2.488
tau = 1.5 * (t2 - t1)               # τ = 5.94
theta = t2 - tau                    # Ɵ = 4

print("Ganho: ", k, "Constante de Tempo: ", tau, "Tempo de atraso: ", theta)


