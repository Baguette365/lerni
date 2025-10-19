import flet
import flet as ft
from flet.core.types import TextAlign


def main(page: ft.Page):
    page.title = "Lerni"

    def route_change(route):
        page.views.clear()
        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, shape=ft.CircleBorder()
        )
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Lerni", color=ft.Colors.BLACK),bgcolor="#003049", center_title=True, adaptive=True),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        #page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
def main2(page: ft.Page):
    page.title = "NavigationBar Example"
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, shape=ft.CircleBorder()
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.MINI_CENTER_FLOAT
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Favorites",
            ),
        ]
    )
    page.add(ft.Text("Body!"))


ft.app(main2)