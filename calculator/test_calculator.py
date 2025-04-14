import unittest
from increase_decrease_calculator import calculateIncDec

class TestClass(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(calculateIncDec(200, 190), [[18, -1, 10]])

	def test_case_2(self):
		self.assertEqual(calculateIncDec(190, 200), [[19, 1, 10]])
	
	def test_case_3(self):
		self.assertEqual(calculateIncDec(300, 321), [[14, 1, 15], [15, 1, 6]])

	def test_case_4(self):
		self.assertEqual(calculateIncDec(321, 300), [[13, -1, 15], [14, -1, 6]])
	
	def test_case_5(self):
		self.assertEqual(calculateIncDec(321, 322), [[321, 1, 1]])

	def test_case_6(self):
		self.assertEqual(calculateIncDec(322, 321), [[320, -1, 1]])
	
	def test_case_7(self):
		self.assertEqual(calculateIncDec(88, 160), [[1, 1, 56], [2, 1, 16]])
	
	def test_case_8(self):
		self.assertEqual(calculateIncDec(160, 232), [[2, 1, 56], [3, 1, 16]])
		
if __name__=='__main__':
	unittest.main()

# Some test-cases:
# Ex 1
# currentStiches = 200
# wantedStiches = 190
# Strikk 18 masker, så 2 sammen. Gjør dette 10 ganger.
# [[18, -1, 10]]

# Ex 2
# currentStiches = 190
# wantedStiches = 200
# Strikk 19 masker, øk med 1 maske. Gjør dette 10 ganger.
# [[19, 1, 10]]

# Ex 3
# currentStiches = 300
# wantedStiches = 321
# Du vil øke 21 masker. Dette må gjøres:

# Strikk 14 masker, øk med 1 maske. × 15
# Strikk 15 masker, øk med 1 maske. × 6
# Følg stegene under for å få det helt jevnt.
# [[14, 1, 15], [15, 1, 6]]

# Gjør disse stegene 3 ganger:
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.
# Strikk 15 masker, øk med 1 maske.
# Strikk 14 masker, øk med 1 maske.
# Gjør disse stegene 3 ganger:
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.
# Strikk 15 masker, øk med 1 maske.
# Strikk 14 masker, øk med 1 maske. Gjør dette 2 ganger.

# TODO: Handle multiple instructions

# Ex 4
# currentStiches = 300
# wantedStiches = 321
# Du vil felle 21 masker. Dette må gjøres:

# Strikk 13 masker, så 2 sammen. × 15
# Strikk 14 masker, så 2 sammen. × 6
# Følg stegene under for å få det helt jevnt.

# Gjør disse stegene 3 ganger:
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.
# Strikk 14 masker, så 2 sammen.
# Strikk 13 masker, så 2 sammen.
# Gjør disse stegene 3 ganger:
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.
# Strikk 14 masker, så 2 sammen.
# Strikk 13 masker, så 2 sammen. Gjør dette 2 ganger.

# Ex 5
# Øke med 1

# Ex 6
# Felle med 1

# Ex 7
# Oppskrift på å øke jevnt fra 88 til 160 masker
# Du vil øke 72 masker. Dette må gjøres:

# Strikk 1 maske, øk med 1 maske. × 56
# Strikk 2 masker, øk med 1 maske. × 16

# Ex 8
# Oppskrift på å øke jevnt fra 160 til 232 masker
# Du vil øke 72 masker. Dette må gjøres:

# Strikk 2 masker, øk med 1 maske. × 56
# Strikk 3 masker, øk med 1 maske. × 16
