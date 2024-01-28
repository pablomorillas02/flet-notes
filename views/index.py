import flet as ft
from manager.notes import notes

class Index(ft.UserControl):
    def __init__(self, page, rebuild_index):
        super().__init__()
        self.page = page
        self.rebuild_index = rebuild_index

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

    # Función para editar una nota
    def edit_note(self, e, id):
        self.page.go("/edit/" + str(id))

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
                        on_click=lambda e: self.get_note(e, note.get_title(), note.get_contenido()),
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