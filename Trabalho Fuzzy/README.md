# Trabalho de C213 - Controle Fuzzy
Projeto destinado a mostrar o funcionamento de um sistema de controle de temperatura para estufa de vacinas e materiais biológicos utilizando um controlador Fuzzy.  
O usuário pode observar a temperatura e erro do sistema através de uma interface gráfica que se comunica com o controlador por MQTT.

## Instalação
Abra a pasta que deseja instalar pelo terminal, e clone o repositório:
```
git clone https://github.com/GualterMM/C213_Disciplina.git
```
O projeto se encontra na pasta "Controle Fuzzy". Abra um terminal nessa pasta.
No terminal, crie um ambiente virtual utilizando o comando:
```
python -m venv '.\venv'
```

Ative o ambiente virtual:
```
.\venv\Scripts\activate
```

Instale as dependências do projeto:
```
pip install -r requirements
```

Execute o sistema de controle:
```
python controller.py
```

Em outro terminal, no ambiente virtual, execute a aplicação:
```
python gui.py
```

## Modo de uso
Monitore a temperatura e erro através dos medidores na interface. Caso deseje mudar o Setpoint, insira o novo valor no campo e clique em "Alterar".

## Equipe de Desenvolvimento

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/GualterMM">
        <img src="https://avatars.githubusercontent.com/u/35864822?v=4" width="100px;" alt="Foto do Gualter Machado no GitHub"/><br>
        <sub>
          <b>Gualter Machado</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/IsabelaRezendeB">
        <img src="https://avatars.githubusercontent.com/u/49520751?v=4" width="100px;" alt="Foto da Isabela Rezende no GitHub"/><br>
        <sub>
          <b>Isabela Rezende</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
