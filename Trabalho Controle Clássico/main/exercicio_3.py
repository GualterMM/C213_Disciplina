import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Exercício 3 - Plote a resposta original em relação a estimada na mesma figura e verifique se a aproximação foi satisfatória
# Importando os dados 
mat = loadmat('../TransferFunction5.mat')

# Simulando a resposta da função de transferencia fornecedida
degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

# Definindo as variáveis da função de transferência em primeira ordem
k = 2.488
tau = 5.94
theta = 4

# Construindo a função de transferência
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)

# Montando o sistema
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# Simulando a resposta da função de transferência estimada
time, y = cnt.step_response(5*Hs, T=t1)

# Plotando os gráficos
plt.plot(time, y, label='Saída (função estimada)')
plt.plot(time, saida, label='Saída (função fornecida)', linestyle='dashed')
plt.plot(time, degrau, label='Degrau de entrada')

# Definindo as legendas e título do gráfico
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")
plt.title('Função de transferência fornecida e estimada')

# Configurando opções de exibição do gráfico
plt.grid()
plt.show()