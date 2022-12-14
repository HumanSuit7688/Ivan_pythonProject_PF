import flet as ft
from calc_backup import numb


def calcul(page: ft.Page):
    page.window_width = 350
    page.window_height = 475
    page.title = 'Calculator'
    result = ft.Text(value = '0')
    def number(e):
        if e.control.data == '.':
            result.value += str(e.control.data)
        elif result.value == '0':
            result.value = str(e.control.data)
        else:
            result.value += str(e.control.data)
        page.update()
    def m_function(e):
        result.value += ' ' + str(e.control.data) + ' '
        page.update()
    def func_backsp(e):
        result.value = result.value[:-1]
        page.update()
    def func_del(e):
        result.value = '0'
        page.update()

    def enter(e):
        in1 = result.value.find(' ')
        n1 = result.value[0:in1]
        print(n1)
        n2 = result.value[in1+3:]
        print(n2)
        mark = result.value[in1+1]
        print(mark)
        if mark == '+':
            res = float(n1) + float(n2)
            print(res)
            result.value = str(res)
        elif mark == '-':
            res = float(n1) - float(n2)
            result.value = str(res)
        elif mark == '/':
            res = float(n1) / float(n2)
            result.value = str(res)
        elif mark == '*':
            res = float(n1) * float(n2)
            result.value = str(res)
        page.update()

    row1 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='<<', on_click=func_backsp),
                    ft.ElevatedButton(text='C', on_click=func_del),
                ]
            )
        ]
    )
    row2 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='7', on_click=number, data='7'),
                    ft.ElevatedButton(text='8', on_click=number, data='8'),
                    ft.ElevatedButton(text='9', on_click=number, data='9'),
                    ft.ElevatedButton(text='/', on_click=m_function, data='/')
                ]

            )
        ]
    )
    row3 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='4', on_click=number, data='4'),
                    ft.ElevatedButton(text='5', on_click=number, data='5'),
                    ft.ElevatedButton(text='6', on_click=number, data='6'),
                    ft.ElevatedButton(text='*', on_click=m_function, data='*')
                ]

            )
        ]
    )
    row4 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='1', on_click=number, data='1'),
                    ft.ElevatedButton(text='2', on_click=number, data='2'),
                    ft.ElevatedButton(text='3', on_click=number, data='3'),
                    ft.ElevatedButton(text='-', on_click=m_function, data='-')
                ]

            )
        ]
    )
    row5 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='0', on_click=number, data='0'),
                    ft.ElevatedButton(text='.', on_click=number, data='.'),
                    ft.ElevatedButton(text='+', on_click=m_function, data='+'),
                    ft.ElevatedButton(text='Enter', on_click=enter)
                ]

            )
        ]
    )
    page.add(result, row1, row2, row3, row4, row5)


ft.app(target=calcul)