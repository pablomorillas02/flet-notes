import flet as ft
from manager.notes import notes

class Index(ft.UserControl):
    def __init__(self, page, rebuild_index):
        super().__init__()
        self.page = page
        self.rebuild_index = rebuild_index
        self.dlg_modal = None 

    def build_drawer(self):
        drawer = ft.NavigationDrawer(
            controls=[
                ft.Divider(thickness=2),
                ft.TextButton(
                    "Sobre mí",
                    icon=ft.icons.PERSON_2,
                    on_click=lambda _: self.page.launch_url("https://github.com/pablomorillas02")
                ),
                ft.Divider(thickness=2),
                ft.TextButton(
                    "Ajustes",
                    icon=ft.icons.SETTINGS,
                    on_click=lambda _: self.page.go("/settings")
                )             
            ],
        )

        return drawer

    def open_drawer(self, e):
        self.page.drawer.open = not self.page.drawer.open
        self.page.update()

    def build_appbar(self):
        appBar = ft.AppBar(
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    color=ft.colors.ON_SURFACE_VARIANT,
                    title=ft.Text("Notas!"),
                )
        
        return appBar

    def build_fab(self):
        fab = ft.FloatingActionButton(
                bgcolor=ft.colors.SURFACE_VARIANT,
                content=ft.Icon(
                    name=ft.icons.ADD,
                    color=ft.colors.ON_SURFACE_VARIANT,
                ),
                shape=ft.CircleBorder(),
                on_click=lambda _: self.page.go("/add")
            )
    
        return fab

    # Función para ver una nota
    def get_note(self, e, note_title, note_content):
        ## Alerta
        dlg = ft.AlertDialog(
            title=ft.Text(note_title),
            content=ft.Column(
                [
                    ft.Text(note_content)
                ]
            )    
        )

        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    # Función para borrar una nota
    def delete_note(self, e, id):
        notes.delete_note(id)

        ### SnackBar
        self.page.snack_bar = ft.SnackBar(
            ft.Text(
                "Nota borrada!",
                color=ft.colors.INVERSE_SURFACE
            ),
            bgcolor=ft.colors.ON_INVERSE_SURFACE
        )
        self.page.snack_bar.open = True
        
        self.rebuild_index()

    ## Cerrar el modal
    def close_modal(self, e):
        self.dlg_modal.open = False
        self.page.update()

    ## Manda la edición
    def confirm_edit(self, e, id, new_title, new_content):
        notes.edit_note(id, new_title, new_content)
        self.close_modal(e)
        self.rebuild_index()

    def get_note_by_id(self, id):
        for note in notes.get_notes():
            if note.get_id() == id:
                return note

    # Función para editar una nota
    def edit_note(self, e, id):
        note = self.get_note_by_id(id)

        ## Campos de entrada
        title_field = ft.TextField(
                        label="Título de la nota",
                        value=note.get_title(),
                        multiline=False,
                        border=ft.InputBorder.OUTLINE,
                        border_color=ft.colors.ON_SURFACE_VARIANT
                    )
        content_field = ft.TextField(
                            label= "Contenido de la nota...",
                            value=note.get_contenido(),
                            multiline=True,
                            border=ft.InputBorder.OUTLINE,
                            border_color=ft.colors.ON_SURFACE_VARIANT
                    )

        ## Ventana para editar la nota
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editando nota..."),
            content=ft.Column(
                controls=[
                    title_field,
                    ft.Divider(),
                    content_field
                ],
            ),
            actions=[
                ft.TextButton(
                    content=ft.Text(
                        "Cancelar",
                        color=ft.colors.ON_SURFACE_VARIANT
                    ) ,
                    on_click=self.close_modal
                ),
                ft.TextButton("Confirmar", on_click=lambda e: self.confirm_edit(e, id, title_field.value, content_field.value)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()
                

    def build_controls(self):
        controls = [
            lv := ft.ListView(
                expand=True,
                controls=[
                    ## Ítem
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.NOTE),
                        title=ft.Text(note.get_title()),
                        subtitle=ft.Text(note.get_contenido()),
                        on_click=lambda e, title=note.get_title(), content=note.get_contenido(): self.get_note(e, title, content),
                        trailing=ft.PopupMenuButton(
                            icon=ft.icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(
                                    text="Editar",
                                    icon=ft.icons.EDIT,
                                    on_click=lambda e, id=note.get_id(): self.edit_note(e, id)
                                ),
                                ft.PopupMenuItem(
                                    text="Borrar",
                                    icon=ft.icons.DELETE,
                                    on_click=lambda e, id=note.get_id(): self.delete_note(e, id)
                                ),
                            ],
                        ),
                    )   
                    for note in notes.get_notes()
                ]
            )
        ]

        return controls