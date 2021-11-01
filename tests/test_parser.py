﻿import unittest
from endplay.parsers import *

from endplay import config
config.use_unicode = False

class TestPBN(unittest.TestCase):
	pass

script1 = """
/*
 * We should support
 * multiline comments
*/
generate		10000 // number of hands to generate
produce	/*hi*/	25
vulnerable		ew
dealer			west
predeal			south SAQ542, HKJ87, D32, CAK
west1n =		shape(west, any 4333 + any 4432 + any 5332 - 5xxx - x5xx) &&
					hcp(west)>14 && hcp(west)<18
# west has at least 5 hearts
west1h =		hearts(west)>= 5 // that was here
west1s =		spades(west)>= 5
west1c =		(not west1n) && hcp(west)>10 && clubs(west)>=3
					&& (not west1h) && (not west1s) && (not west1d)
north2d =		(hcp(north)>5 && hcp(north)<12) &&
					shape(north, xx6x + xx7x - any 4xxx - any 5xxx)
condition		west1c && north2d
action			printall
"""

class TestDealer(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.parser = DealerParser()
	def test_script(self):
		parser = self.parser
		res = parser.parse_string(script1)
		# No exception thrown, should be fine right...

	def test_expr(self):
		parser = self.parser
		parser.parse_expr("shape(north, 4432) && hcp(north) == 10")
