from PySimpeGUI cccimport PySimpleGUI as sg

# layout

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')]
]

#janela
janela = sg.Window('Tela de login', layout)
janelas = sg.Window
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'pedro'
            and valores['senha'] == '123':
            print('Bem Vindo')