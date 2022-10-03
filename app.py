from time import sleep
import flet
from flet import Page, Text, Row, TextField, ElevatedButton


def main(page: Page):
    # page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # Create our variable wich is  a regular Python calss -> Controls
    # t = Text(value="Counter App", color="green")
    # # Append / Add the control to the page
    # # page.controls.append(t)
    # # # Update the ui of that specific page -> See the changes
    # # page.update()
    # page.add(t)
    # while 0 == 0:
    #     for i in range(10):
    #         t.value = f"Step {i}"
    #         page.update()
    #         sleep(1)
    #     if (i == 9):
    #         sleep(1)
    #         t.value = 0
    # page.update()

    # page.add(
    #     Row(controls=[
    #         Text(value="A", color="yellow"),
    #         Text(value="B", color="blue"),
    #         TextField(label="Youre Name :"),
    #         ElevatedButton(text="Say My Name!"),
    #         Text(value="C", color="white"),
    #     ],
    #         alignment="center",
    #     )
    # )

    # for i in range(20):
    #     page.controls.append(Text(value=f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     sleep(0.3)

    def buttom_clicked(e):
        page.add(Text(value="Clicked!"),)

    page.add(ElevatedButton(text="Click me !", on_click=buttom_clicked))


flet.app(target=main)
