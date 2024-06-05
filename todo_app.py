import flet as fl
import time
from flet import *


def main(page: Page):
    def clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = TextField(hint_text="What's needs to be done ?", color="blue", width=300)
    page.add(Row([new_task, ElevatedButton('add', on_click=clicked)]))


app(target=main)
