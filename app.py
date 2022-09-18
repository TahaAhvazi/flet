from cgitb import text
from ctypes import alignment
import flet
from flet import IconButton, Page, Row, TextField, icons, Text


def main(page: Page):
    page.title = "Taha Flet Counter App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    txt_number = Text(value=0)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.ADD, on_click=plus_click),
                txt_number,
                IconButton(icons.REMOVE, on_click=minus_click),
            ],
            alignment="center"
        )
    )


flet.app(target=main)
