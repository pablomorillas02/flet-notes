import flet as ft
import uuid
from manager.notes import notes

class Add(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        # Campos de entrada
        self.note_title = None
        self.note_content = None

    # Creación de la tarea
    def create_note(self, e, note_title, note_content):
        id = uuid.uuid4() # identificador único
        notes.create_note(note_title, note_content, id)

        self.page.go("/")

    def build_appbar(self):
        button = ft.IconButton(
                    icon=ft.icons.CHECK,
                    icon_color=ft.colors.ON_SURFACE_VARIANT,
                    on_click=lambda e: self.create_note(e, self.note_title.value, self.note_content.value),
                )

        appBar = ft.AppBar(
            bgcolor=ft.colors.SURFACE_VARIANT,
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color=ft.colors.ON_SURFACE_VARIANT,
                on_click=lambda _: self.page.go("/")
            ),
            actions=[
                button
            ]
        )

        return appBar

    def build_controls(self):
        # Creación de los elementos definidos
        self.note_title = ft.TextField(
            label="Título de la nota",
            multiline=False,
            border=ft.InputBorder.NONE,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            color=ft.colors.INVERSE_SURFACE
        )

        self.note_content = ft.TextField(
            label= "Contenido de la nota...",
            multiline=True,
            border=ft.InputBorder.NONE,
            icon=ft.icons.TEXT_FIELDS,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            color=ft.colors.INVERSE_SURFACE
        )

        controls = [
            self.note_title,
            ft.Divider(),
            self.note_content,
        ]

        return controls