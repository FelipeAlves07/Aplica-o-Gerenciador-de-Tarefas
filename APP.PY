import PySimpleGUI as sg

# Criando o layout

def criar_janela_inicial(): # função
    sg.theme('DarkGrey9')  # tema da apicação
    linha = [ # onde será escrito a tarefa
        [sg.Checkbox(''),sg.Input('')]    # onde será marcado tarefas conclusas ou não
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Reset')]
    ]

    return sg.Window('Meus Compromissos',layout=layout,finalize=True) # será usado na criação de jenela

# Criando a janela

janela = criar_janela_inicial()

# Criando regras da janela

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    if event == 'Reset':
        janela.close()
        janela = criar_janela_inicial()