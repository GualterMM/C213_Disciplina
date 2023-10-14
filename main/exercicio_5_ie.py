# Exercício 5 - Comparação do métodos tradicional do Modelo Interno (IMC) com os métodos da Integral do Erro
import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# Definindo as variáveis da função de transferência em primeira ordem
k = 2.488
tau = 5.94
theta = 4

# MÉTODO Novo - Integral do Erro
kp = (1 / ((theta / tau) + 0.2) / k) - 0.1
ti = ((((0.3 * (theta / tau)) + 1.2)/((theta / tau) + 0.08)) * theta)
td = ((1 / (90 * (theta / tau))) * theta)

# Escrevendo a função de transferência da planta
num = np.array([k])
den = np.array([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# Controlador proporcional
numkp = np.array([kp])
denkp = np.array([1])

# Controlador integral
numki = np.array([kp])
denki = np.array([ti,0])

# Controlador derivativo
numkd = np.array([kp*td,0])
denkd = np.array([1])

# Construindo o controlador PID
Hkp = cnt.tf(numkp , denkp)
Hki = cnt.tf(numki , denki)
Hkd = cnt.tf(numkd , denkd)
Hctrl1 = cnt.parallel (Hkp , Hki)
Hctrl = cnt.parallel (Hctrl1 , Hkd)
Hdel = cnt.series (Hs , Hctrl)

# Fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

t = np.linspace(0 , 60 , 100)
( t , y ) = cnt.step_response (5 * Hcl, t )
plt.plot (t , y)
plt.xlabel (' t [ s ]')
plt.ylabel('Amplitude')
plt.title('Controle PID')

plt.grid()
plt.show()
