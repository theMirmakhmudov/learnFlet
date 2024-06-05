import flet as ft
from flet import *


def main(page: Page):
    page.add(Column(
        controls=[
            Text(value="Hello", color="red"),
            Text(value="Salom", color="green"),
            Text(value="Privet", color="blue")
        ]
    ))


ft.app(target=main)
