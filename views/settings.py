import flet as ft
from flet_contrib.color_picker import ColorPicker
from manager.main_color import color, file

class Settings(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.color_picker = ColorPicker(color=color)
        self.switch_mode = False if page.theme_mode == ft.ThemeMode.DARK else True

    def change_theme(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )

        self.page.update()

    def change_color(self, e):
        color = self.color_picker.hex.value

        # Sobreescribir el color del tema para guardarlo
        with open (file, "w") as f:
            f.writelines(color)

        self.page.theme = ft.Theme(color_scheme_seed=color)
        self.page.update()

    def build_appbar(self):
        appBar = ft.AppBar(
            bgcolor=ft.colors.SURFACE_VARIANT,
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color=ft.colors.ON_SURFACE_VARIANT,
                on_click=lambda _: self.page.go("/")
            ),
        )

        return appBar

    def build_controls(self):
        controls = [
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.SafeArea(
                                ft.Text(
                                    "¡Personaliza la interfaz a tu gusto!",
                                    size=20,
                                    weight=ft.FontWeight.BOLD
                                )
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=20,
                                border_radius=10,
                                bgcolor=ft.colors.SURFACE_VARIANT,
                                content=self.color_picker
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton(
                                "Aplicar",
                                on_click=self.change_color
                            )
                        ]
                    ),
                    ft.Container(
                        content=ft.Divider(thickness=2)
                    ),
                    ft.Container(
                        expand=False,
                        padding=20,
                        border_radius=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.SafeArea(
                                            ft.Text(
                                                "¡Alterna el tema entre claro y oscuro!",
                                                size=14,
                                                weight=ft.FontWeight.BOLD
                                            )
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Switch(
                                            value=self.switch_mode,
                                            on_change=self.change_theme
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            ),
        ]

        return controls