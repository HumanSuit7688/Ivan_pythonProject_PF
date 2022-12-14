import flet as ft


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
    row1 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='/'),
                    ft.ElevatedButton(text='*'),
                    ft.ElevatedButton(text='-'),
                    ft.ElevatedButton(text='+')
                ]

            )
        ]
    )
    row2 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='7'),
                    ft.ElevatedButton(text='8'),
                    ft.ElevatedButton(text='9')
                ]

            )
        ]
    )
    row3 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='4'),
                    ft.ElevatedButton(text='5'),
                    ft.ElevatedButton(text='6')
                ]

            )
        ]
    )
    row4 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='1'),
                    ft.ElevatedButton(text='2'),
                    ft.ElevatedButton(text='3')
                ]

            )
        ]
    )
    row5 = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text='0'),
                    ft.ElevatedButton(text='.'),
                    ft.ElevatedButton(text='Enter')
                ]

            )
        ]
    )
    page.add(result, row1, row2, row3, row4, row5)


ft.app(target=calcul)