from exceptions import Exception

class SelfDependencyException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class FilenameExistException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class UpdateDeniedException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class AddingAttachmentDenied(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class AddingModuleDenied(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class SingletonCopyException(Exception):
	def __init__(self):
		""
	def __str__(self):
		return repr("SDK can't be copied")
