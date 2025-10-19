"""
study with ONE app only
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class lerni(toga.App):
	def startup(self):
		srsPage = toga.Box(style=Pack(direction=COLUMN, padding=10))
		srsPage.add(toga.Label('Contenu de la page 1'))
		srsPage.add(toga.Button('Bouton page 1', on_press=self.action))
		
		pomodoroPage = toga.Box(style=Pack(direction=COLUMN, padding=10))
		pomodoroPage.add(toga.Label('Contenu de la page 2'))
		pomodoroPage.add(toga.TextInput(placeholder='Texte ici'))
		
		musicPage = toga.Box(style=Pack(direction=COLUMN, padding=10))
		musicPage.add(toga.Label('Contenu de la page 3'))
		
		notesPage = toga.Box(style=Pack(direction=COLUMN, padding=10))
		notesPage.add(toga.Label('Contenu de la page 3'))
		
		# Créer un conteneur à onglets
		container = toga.OptionContainer(
			content=[
				('srs', srsPage),
				('pomodoro', pomodoroPage),
				('music', musicPage),
				('notes', notesPage)
			]
		)
		
		self.main_window = toga.MainWindow(title=self.formal_name)
		self.main_window.content = container
		self.main_window.show()
		
	def action(self, control):
		print("ok")
		
		


def main():
	return lerni()
