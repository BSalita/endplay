__all__ = ["Denom"]

from enum import IntEnum
from typing import Iterator

use_symbols = False

class Denom(IntEnum):
	"Encoding for suits and contract denomination"
	spades		= 0
	hearts		= 1
	diamonds	= 2
	clubs		= 3
	nt			= 4

	@property
	def use_symbols(self) -> bool:
		global use_symbols
		return use_symbols
	@use_symbols.setter
	def use_symbols(self, val: bool) -> None:
		global use_symbols
		use_symbols = val

	@staticmethod
	def find(name: str) -> 'Denom':
		"Convert a string value into a Denom object"
		try:
			return Denom("SHDCN".index(name[0].upper()))
		except ValueError:
			raise ValueError(f"Could not convert {name} into a Denom object")

	@staticmethod
	def bidorder() -> Iterator['Denom']:
		":return: An iterator over all the denominations in the order they appera in a bidding box"
		yield from [Denom.clubs, Denom.diamonds, Denom.hearts, Denom.spades, Denom.nt]

	@staticmethod 
	def suits(reverse: bool = False) -> Iterator['Denom']:
		"""
		:param reverse: If true, return suits in the order clubs -> spades
		:return: An iterator over the four suits
		"""
		r = range(3,-1,-1) if reverse else range(4)
		for i in r:
			yield Denom(i)

	def is_suit(self) -> bool:
		":return: True if the denomination is not notrumps"
		return self in Denom.suits()

	def is_major(self) -> bool:
		":return: True if the denomination is spades or hearts"
		return self in [ Denom.spades, Denom.hearts ]

	def is_minor(self) -> bool:
		":return: True if the denomination is diamonds or clubs"
		return self in [ Denom.diamonds, Denom.clubs ]

	@property
	def abbr(self) -> str:
		":return: A short identifier for the denomination"
		if self == Denom.nt:
			return "NT"
		elif self.use_symbols:
			return "♠♥♦♣"[self]
		else:
			return "SHDC"[self]
