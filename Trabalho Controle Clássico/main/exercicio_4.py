import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Exercício 4 - Levante os valores de erro da planta em malhar aberta e fechada, fazendo comentários sobre os resultados
# Importando os dados 
mat = loadmat('../TransferFunction5.mat')
saida = mat.get('saida')
degrau = mat.get('degrau')

# Definindo as variáveis da função de transferência em primeira ordem
k = 2.488
tau = 5.94
theta = 4

# Escrevendo a função de transferência da planta
num = np. array([k])
den = np. array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)

# Simulando funções para malha aberta e fechada, respectivamente
Hs = cnt.series(H, H_pade)
Hmf = cnt.feedback(Hs, 1)

# Plotando o sinal da malha aberta
time = np.linspace(0, 180, 361)
(t, y1) = cnt.step_response(5 * Hs, time)
plt.plot(time, y1, label='Erro (malha aberta)')

# Plotando o sinal da malha fechada
(t, y2) = cnt.step_response(5 * Hmf, time)
plt.plot(time, y2, label='Erro (malha fechada)')

# Plotando o degrau para comparação de sinais
plt.plot(time, degrau, label='Degrau de entrada')

# Definindo as legendas e título do gráfico
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Comparação de erro entre malha aberta e fechada')
plt.legend(loc="upper left")
plt.grid(True)

# Exibindo o gráfico
plt.grid()
plt.show()

# Calculando o erro em malha aberta e fechada
erro_ma = 5 - max(saida)
erro_mf = 5 - 3.58
print(f'Erro da malha aberta: {erro_ma[0]}')
print(f'Erro da malha fechada: {erro_mf}')