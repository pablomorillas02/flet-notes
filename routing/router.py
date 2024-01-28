import flet as ft
from views.index import Index
from views.add import Add
from views.settings import Settings

def views_handler(page, rebuild_index, id):    
    # Creación de vistas
    index = Index(page, rebuild_index)
    add = Add(page)
    settings = Settings(page)

    # Asignación del drawer a la página principal
    page.drawer = index.build_drawer()

    return {
        "/": ft.View(
            route="/",
            appbar=index.build_appbar(),
            floating_action_button=index.build_fab(),
            controls=index.build_controls(),
            drawer=page.drawer,
        ),
        "/add": ft.View(
            route="/add",
            appbar=add.build_appbar(),
            controls=add.build_controls(),
        ),
        "/settings": ft.View(
            route="/settings",
            appbar=settings.build_appbar(),
            controls=settings.build_controls()
        ),
    }