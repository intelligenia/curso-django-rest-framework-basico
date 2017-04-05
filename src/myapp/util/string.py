# -*- coding: utf-8 -*-

import string
import random


########################################################################
########################################################################

CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CAPITAL_LETTERS_NO_LOOKALIKES = "ABCDEFGHJKLMNPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
LOWER_LETTERS_NO_LOOKALIKES = "abcdefghjkmnpqrstuvwxyz"
NUMBERS = "1234567890"
NUMBERS_NO_LOOKALIKES = "23456789"

# Mayúsculas, minúsculas
LETTERS = (CAPITAL_LETTERS, LOWER_LETTERS)

# Mayúsculas, minúsculas, números
LETTERS_NUMBERS = (CAPITAL_LETTERS, LOWER_LETTERS, NUMBERS)

# Mayúsculas, números
CAPITAL_NUMBERS = (CAPITAL_LETTERS, NUMBERS)

# Minúsculas, números
LOWER_NUMBERS = (LOWER_LETTERS, NUMBERS)

# Mayúsculas nl, minúsculas nl, números nl
LETTERS_NUMBERS_NO_LOOKALIKES = (CAPITAL_LETTERS_NO_LOOKALIKES, LOWER_LETTERS_NO_LOOKALIKES, NUMBERS_NO_LOOKALIKES)

# Mayúsculas nl, números nl
CAPITAL_NUMBERS_NO_LOOKALIKES = (CAPITAL_LETTERS_NO_LOOKALIKES, NUMBERS_NO_LOOKALIKES)

# MinúscUlas nl, números nl
LOWER_NUMBERS_NO_LOOKALIKES = (LOWER_LETTERS_NO_LOOKALIKES, NUMBERS_NO_LOOKALIKES)


def random_string_generator(length, char_groups=LETTERS_NUMBERS):
	"""
	Devuelve una cadena con tantos caracteres aleatorios como se indiquen en la
	llamada.
	El conjunto de caracteres a incluir se indicará como una lista de cadenas
	en las que se concatenerán.
	Se espera que lo que se recibe en char_groups sea un listado de cadenas
	de caracteres correcta.
	
	"""
	
	return ''.join(random.choice("".join(char_groups)) for x in range(length))
