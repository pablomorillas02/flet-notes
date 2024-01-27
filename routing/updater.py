import flet as ft
from views.index import Index

# Esta función vuelve a crear una vista Index
def update_index(page, rebuild_index):
    index = Index(page, rebuild_index)

    # Asignación del drawer a la página principal, como en el enrutado
    page.drawer = index.build_drawer()

    view = ft.View(
        route="/",
        appbar=index.build_appbar(),
        floating_action_button=index.build_fab(),
        controls=index.build_controls(),    
        drawer=page.drawer    
    )

    return view