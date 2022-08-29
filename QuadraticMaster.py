import PySimpleGUI as sg


def complete_equation(a,b,c):

    D = b ** 2 - 4 * a * c

    if D > 0:
        n = 2
        window['n'].update(str(n))
        x1 = (-b + D ** 0.5)/ 2 * a
        x2 = (-b - D ** 0.5)/ 2 * a
        return round(x1,2), round(x2,2)
    else:
        n = None
        window['n'].update(str(n))
        x1 = None
        x2 = None
        return x1, x2

def incomplete_equation(a,b,c):
    if b == 0 and c == 0:
        n = 1
        window['n'].update(str(n))
        x1 = 0
        x2 = None
        return x1, x2

    elif b == 0 and c != 0:
        if (-c / a) > 0:
            n = 2
            window['n'].update(str(n))
            x1 = (-c / a)**0.5
            x2 = -(-c / a)**0.5
            return round(x1,2), round(x2,2)

        else:
            n = None
            window['n'].update(str(n))
            x1 = None
            x2 = None
            return x1, x2
    else:
        n = 2
        window['n'].update(str(n))
        x1 = 0
        x2 = -b / a
        return round(x1,2), round(x2,2)

sg.theme('Dark Brown 5')

layout = [
     [sg.T('a', key='lbl_a',font='consalo 14'), sg.I('', key='edit_a', size=(7,1),pad=(10,10)),
      sg.T('b', key='lbl_b', font='consalo 14'), sg.I('', key='edit_b', size=(7,1),pad=(10,10)),
     sg.T('c', key='lbl_c', font='consalo 14'), sg.I('', key='edit_c', size=(7,1),pad=(10,10)),
      sg.B('Рассчитать', key='calc', border_width=3, pad=(15,15))],
     [sg.T('Количество корней уравнения', key='lbl_n', font='consalo 14'), sg.I('', key='n', size=(5,1),pad=(10,10))],
     [sg.T('x1', key='lbl_x1', font='consalo 14'), sg.I('', key='x1', size=(7,1),pad=(10,10)),
     sg.T('x2', key='lbl_x2', font='consalo 14'), sg.I('', key='x2', size=(7,1),pad=(10,10))]
  ]

window = sg.Window('QuadraticMaster', layout, size=(450,180))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == 'calc':
        a = float(values['edit_a'])
        b = float(values['edit_b'])
        c = float(values['edit_c'])

        while a > 0:
            if b != 0 and c!= 0:
                x1, x2 = complete_equation(a,b,c)
                window['x1'].update(str(x1))
                window['x2'].update(str(x2))
                break
            else:
                
                x1,x2 = incomplete_equation(a,b,c)
                window['x1'].update(str(x1))
                window['x2'].update(str(x2))
                break
        else:
            sg.popup_error('Введите `а` больше нуля')

       
window.close()
