class letterCaseNotFoundException(Exception):
	def __init__(self, lettercase, message='Case must be "upper", "lower", or "all"'):
		self.lettercase = lettercase
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'Case was "{self.lettercase}" - {self.message}'

class specialCharacterNotSpecifiedException(Exception):
	def __init__(self, special, message='Special must be type bool - True or False'):
		self.special = special
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'Special was "{self.special}" - {self.message}'

class numberNotOperableException(Exception):
	def __init__(self, message='Arguments must be int or float'):
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'Could not perform operation on argument - {self.message}'

class notEnoughInfoException(Exception):
	def __init__(self, message='Not enough information was given.'):
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'Could not perform specified function - {self.message}'

class randomCalculationFailedException(Exception):
	def __init__(self, custom, message='Random was called too many times',):
		self.message = message
		self.custom = custom
		super().__init__(self.message)
	def __str__(self):
		return f'Could not perform random generation - {self.message} - {self.custom}'

class invalidSeedException(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'Seed was invalid - {self.message}'

class duplicatePlayerException(Exception):
	def __init__(self, player):
		self.object = player
		super().__init__(self.object)
	def __str__(self):
		return f'More than one player object was created. Original object - {self.object}'

class duplicateBoardException(Exception):
	def __init__(self, board):
		self.object = board
		super().__init__(self.object)
	def __str__(self):
		return f'More than one board object was created. Original object - {self.object}'


class StdErr1(Exception):
	def __init__(self, module):
		self.module = module
		super().__init__(self.module)
	def __str__(self):
		return f'std namespace err1: {self.module} is not a valid python namespace'


class MainEntryNotFoundError(Exception):
	def __init__(self, filename):
		self.filename = filename
		super().__init__(self.filename)
	def __str__(self):
		return f'No main function suitable for an entry point found in file {self.filename}'