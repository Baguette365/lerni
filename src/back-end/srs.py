class Card:
	def __init__(self, front, back, bonus="this bonus does not exist btw"):
		self.box = 0
		self.difficulty = 1  # 1 equal nothing, normal, but the more you go down to 0 the more difficult this card is
		self.front = front
		self.bonus = bonus
		self.back = back


class Deck:
	def __init__(self, name):
		self.cards = []
		self.name = name
	
	def add_card(self, card):
		self.cards.append(card)
	
	def add_cards(self, cards):
		for card in cards:
			self.cards.append(card)


class CardStudier:
	def __init__(self):
		self.decks = []
		self.global_day = 0  # adding 1 every day
	
	def review_card(self, difficulty, card):  # difficulty must be -1 for no, 0 for hard or 1 for yes
		match difficulty:
			case 1:
				card.box += 2
				card.box += 1
				card.box = 1