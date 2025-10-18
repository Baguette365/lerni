class Card:
	def __init__(self, front, back, bonus="this bonus does not exist btw"):
		self.next_date = 0
		self.difficulty = 1 # 1 equal nothing, normal, but the more you go down to 0 the more difficult this card is
		self.front=front
		self.bonus=bonus
		self.back=back
		
		
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
		self.decks=[]
		
	def review_card(self):
		pass