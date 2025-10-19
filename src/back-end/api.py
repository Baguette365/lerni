import srs

def CreateCard(front, back, bonus="this bonus does not exist btw"):
	return srs.Card(front, back, bonus)

def GetCard(card: srs.Card):
	if card.bonus == "this bonus does not exist btw":
		return card.front, card.back, card.bonus
	else:
		return card.front, card.back

