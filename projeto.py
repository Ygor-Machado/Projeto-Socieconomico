import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from datetime import date


#Criar as janelas e estilos(layout)

def buscar_arquivo(theme):
    sg.theme(theme)
    layout_fb = [
                [sg.T('Escolha um arquivo') , sg.Input(k='-input-'), sg.FileBrowse('Browse', k='-FILEBROWSE-', button_color='blue')],
                 [sg.Ok('Continuar', button_color='blue'), sg.Cancel('Sair', button_color='red')]

                 ]

    return sg.Window('Perfil Socioeconômico', layout=layout_fb, finalize=True, size=(625, 300))

def janela_pesquisa():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Escolha o grafico a ser mostrado')],
    
        [sg.LB(values=list[0:], key = 'gr', bind_return_key=True, enable_events = True, no_scrollbar=True, s=(40, 4))],

    ]
    janela1 = sg.Window('Grafico', layout, finalize = True)
    return janela1

janela0 ,janela1 = buscar_arquivo('DarkBlack'), None

    
while True:
    window, event, values = sg.read_all_windows()

    #Quando janela for fechada
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if window == janela0 and event == 'Continuar':
        formularioCSV = values['-FILEBROWSE-']

        lerCSV = pd.read_csv(formularioCSV)
        df = pd.DataFrame(lerCSV)
        df['Data de nascimento'] = ''
        linha = 0

        for valor in df.values:
            if valor[9] == 'Janeiro':
                valor[9] = 1
            elif valor[9] == 'Fevereiro':
                valor[9] = 2
            elif valor[9] == 'Março':
                valor[9] = 3
            elif valor[9] == 'Abril':
                valor[9] = 4
            elif valor[9] == 'Maio':
                valor[9] = 5
            elif valor[9] == 'Junho':
                valor[9] = 6
            elif valor[9] == 'Julho':
                valor[9] = 7
            elif valor[9] == 'Agosto':
                valor[9] = 8
            elif valor[9] == 'Setembro':
                valor[9] = 9
            elif valor[9] == 'Outubro':
                valor[9] = 10
            elif valor[9] == 'Novembro':
                valor[9] = 11
            elif valor[9] == 'Dezembro':
                valor[9] = 12

            df.loc[linha, 'Data de nascimento'] = f'{valor[8]}/{valor[9]}/{valor[10]}'
            linha += 1


        df.drop('Carimbo de data/hora', inplace=True, axis=1)
        df.drop('3. Informe os 7 últimos dígitos do seu RA: (109nnnxxxxxxx) ', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em casa]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [No trabalho]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Na escola]', inplace=True, axis=1)
        df.drop('23-1 .Onde você utiliza microcomputadores (notebooks e desktops)? [Em outros lugares]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos profissionais:]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para trabalhos escolares:]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para entretenimento (músicas, vídeos, redes sociais, etc):]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para comunicação por e-mail:]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para operações bancárias:]', inplace=True, axis=1)
        df.drop('23-2.Com qual finalidade você utiliza microcomputadores (notebooks e desktops)? [Para compras eletrônicas:]', inplace=True, axis=1)
        df.drop('42. Escreva algumas linhas sobre sua história e seus sonhos de vida.', inplace=True, axis=1)

        ano_atual = date.today().year
        listaIdades = []

        for linhaX in df.values:
            calcIdades = ano_atual - linhaX[8]
            listaIdades.append(calcIdades)


        df.insert(2, '3. Idades?', listaIdades, allow_duplicates=True)


        list = df.columns[0:]

        janela0.hide()
        janela1 = janela_pesquisa()


    if event == 'gr':
        plt.clf()
        params = {
            'legend.fontsize': 8,
            'legend.loc': 'upper left',
            'legend.framealpha': 0,
            'legend.handlelength': 1.0,
            'legend.handleheight': 0.7
        }
        plt.rcParams.update(params)
        valor = values[event]
        cont = df[valor]
        nomegr = valor[0]
        grafico = cont.value_counts()
        plt.pie(grafico, autopct='%1.0f%%')
        plt.title(nomegr)
        plt.legend(grafico.index)
        plt.show()

janela0.close()