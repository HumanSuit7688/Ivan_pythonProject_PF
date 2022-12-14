import flet as ft
from calc_backup import numb

# def hard_main(page: ft.Page):
#     page.window_width = 800
#     page.window_height = 500
#     def add_clicked(e):
#         tasks_view.controls.append(ft.Checkbox(label=new_task.value))
#         new_task.value = ""
#         view.update()
#
#     new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
#     tasks_view = ft.Column()
#     view=ft.Column(
#         width=600,
#         controls=[
#             ft.Row(
#                 height=400,
#                 controls=[
#                     new_task,
#                     ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked, autofocus=True),
#                 ],
#             ),
#             tasks_view,
#         ],
#     )
#
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.add(view)
#
#
# ft.app(target=hard_main)


def calcul(page: ft.Page):
    page.window_width = 350
    page.window_height = 475
    page.title = 'Calcul'
    result = ft.Text(value = '0')
    def number(e):
        if e.control.data == ',':
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
                    ft.ElevatedButton(text=',', on_click=number, data=','),
                    ft.ElevatedButton(text='+', on_click=m_function, data='+'),
                    ft.ElevatedButton(text='Enter', on_click=enter)
                ]

            )
        ]
    )
    page.add(result, row1, row2, row3, row4, row5)


ft.app(target=calcul)