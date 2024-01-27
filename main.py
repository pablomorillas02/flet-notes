import flet as ft
import uuid
from routing.router import views_handler
from routing.updater import update_index
from manager.notes import notes
from manager.main_color import color

def main(page: ft.Page):
    # Título
    page.title = "Notas!"

    # Tema
    page.theme_mode = ft.ThemeMode.SYSTEM # Tema del sistema

    # Scroll
    page.auto_scroll = False
    page.scroll = ft.ScrollMode.HIDDEN

    # Color primario del tema
    page.theme = ft.Theme(color_scheme_seed=color)

    # Actualizar vista
    def rebuild_index():
        view = update_index(page, rebuild_index)
        page.views[-1] = view # la vista que estamos viendo esta siempre al final de la lista

        page.update()

    # Routing
    ## Cambios en la ruta
    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page, rebuild_index)[page.route]
        )

    ## Vuelta hacia atrás
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)    

    ## Lógica
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

    page.update()


ft.app(main)
