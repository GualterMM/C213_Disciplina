# Exercício 5 - Comparação do métodos tradicional do Modelo Interno (IMC) com os métodos da Integral do Erro
import numpy as np
import control as cnt
import matplotlib.pyplot as plt

def solve_ie(k, tau, theta):
    try:
        kp = (1 / ((theta / tau) + 0.2) / k)
        ti = ((((0.3 * (theta / tau)) + 1.2)/((theta / tau) + 0.08)) * theta)
        td = ((1 / (90 * (theta / tau))) * theta)
    except:
        return "Formato inválido para os parâmetros númericos"
    else:
        return kp, ti, td

def solve_imc(k, tau, theta):
    try:
        lambda_var = (0.8 * theta) + 0.1
        kp = ((2 * tau + theta) / (k * (2 * lambda_var + theta)))
        ti = tau + (theta / 2)
        td = (tau * theta) / (2 * tau + theta)
    except:
        return "Formato inválido para os parâmetros númericos"
    else:
        return kp, ti, td

def create_plant_tf(k, tau, theta):
    try:
        num = np.array([k])
        den = np.array([tau , 1])
        H = cnt.tf(num , den)
        n_pade = 20
        ( num_pade , den_pade ) = cnt.pade ( theta , n_pade )
        H_pade = cnt.tf( num_pade , den_pade )
        Hs = cnt.series (H , H_pade)
    except:
        return "Formato inválido para os parâmetros númericos"
    else:
        return Hs

def create_pid_control_system(kp, ti, td, sp, Hs):
    try:
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

        t = np.linspace(0 , 100 , 100)
        ( t , y ) = cnt.step_response (sp * Hcl, t )
    except:
        return "Formato inválido para os parâmetros númericos"
    else:
        return t, y
    
def plot_ft(t, y):
    plt.plot (t , y)
    plt.xlabel (' t [ s ]')
    plt.ylabel('Amplitude')
    plt.title('Controle PID')

    plt.grid()
    plt.show()

def get_pid_params():
    k, tau, theta, sp = None, None, None, None
    while k is None and tau is None and theta is None and sp is None:
        try:
            print("Entre com os parâmetros abaixo:")
            k = float(input("K (Ganho estático em malha aberta): "))
            tau = float(input("Tau (Constante de tempo): "))
            theta = float(input("Theta (Atraso de transporte): "))
            sp = float(input("Setpoint (Valor de referência): "))
        except:
            print("Formato inválido para os parâmetros númericos. Insira apenas números decimais.")
        else:
            return k, tau, theta, sp

def main():
    option = None

    while option != 3:
        print("Selecione o número do método de sintonia do controlador PID desejado:")
        print("{1}: Método do Modelo Interno (IMC)")
        print("{2}: Método da Integral de Erro Absoluto (IAE)")
        print("{3}: Sair")
        try:
            option = int(input())
        except ValueError:
            pass

        if option == 1:
            k, tau, theta, sp = get_pid_params()
            kp, ti, td = solve_imc(k, tau, theta)
            Hs = create_plant_tf(k, tau, theta)
            t, y = create_pid_control_system(kp, ti, td, sp, Hs)
            plot_ft(t, y)
            break
        elif option == 2:
            k, tau, theta, sp = get_pid_params()
            kp, ti, td = solve_ie(k, tau, theta)
            Hs = create_plant_tf(k, tau, theta)
            t, y = create_pid_control_system(kp, ti, td, sp, Hs)
            plot_ft(t, y)
            break
        elif option == 3:
            exit()
        else:
            print("Opção inválida")
        

if __name__ == "__main__":
    main()
