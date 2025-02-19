<p >
    <h1 align=center>Activity Checker<h1>
</p>

## ***Atenção:

O objetivo deste bot é apenas ajudar quem quer "farmar" pontos e manter presença em live, ele precisa que a live esteja com a janela aberta em primeiro plano.

## Como instalar:

1- Este script precisa que você tenha o Python instalado na sua máquina, você pode fazer o download na página oficial do [Python - Downloads](https://www.python.org/downloads/) baixando a versão mais atual do programa.
2- Em seguida você deve executar o script, ele fará sozinho a instalação das dependências necessárias para a execução do bot (No caso apenas o [pyautogui](https://pyautogui.readthedocs.io/en/latest/) )
3- Após a instalação das dependências o Python pode apresentar um erro, execute novamente e ele deve funcionar corretamente, caso não crie uma Issue com o log do erro ou se souber como resolver pode enviar um Pull Request, ambos serão mt bem vindos!

## Configurações:

- Para realizar alterações no projeto basta abrir o arquivo em um editor de texto e alterar o valor das variáveis. Todo o código está comentado para facilitar a edição, as principais variaveis são:

    - **mensagens** - É uma lista python que contem as mensagens que serão digitadas, recomendo que não use acentos gráficos para evitar problemas na digitação, você pode criar quantas mensagens quiser e deixar o python fazer o serviço

    - **intervalo** - Intervalo é randomico que define o tempo entre as mensagens, são dois valores inteiros e o pytthon irá escolher algum valor entre estes dois aleatóriamente, recomendo que não use tempos inferiores a 30 segundos, pra evitar que alguma plataforma de strike ou ban. 

- Para parar a execução do programa basta clicar no terminal Python e digitar Ctrl+C ou apenas fechar o terminal.


## Observações:
- Este projeto é uma solução que eu criei pra não perder sorteios e pontos de participação em lives, ele não serve para fins ilicitos
- Este projeto serve pra você poder fazer suas coisas enquanto assiste aquela live marota, sem se preocupar em ficar o tempo todo digitando