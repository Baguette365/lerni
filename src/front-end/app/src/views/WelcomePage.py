import flet as ft
from views import srsPage

class WelcomePage(ft.View):
	def __init__(self):
		super().__init__()
		self.route="/home"
		"""self.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, shape=ft.CircleBorder()
        )"""
		self.controls=[
			ft.AppBar(title=ft.Text("Main Menu", color=ft.Colors.BLACK), bgcolor="#003049", center_title=True,adaptive=True),
		]
		self.navigation_bar = ft.NavigationBar(
			destinations=[
				ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
				ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
				ft.NavigationBarDestination(
					icon=ft.Icons.BOOKMARK_BORDER,
					selected_icon=ft.Icons.BOOKMARK,
					label="Favorites",
				),
			],
			on_change=lambda e: print(self.navigation_bar.page)
		)
			
			