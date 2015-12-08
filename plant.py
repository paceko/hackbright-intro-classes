class Plants(object):
	def __init__(self, name, color, flowering):
		self.name = name
		self.color = color
		self.flowering = flowering
	def set_is_flowering(self, is_flowering):
		self.flowering = is_flowering
			# return ("self.flowering" == False)
		


Pansy = Plants ("pansy", "purple", True)
Tree = Plants("tree", "green", False)

print Pansy.set_is_flowering(True)
print Tree.set_is_flowering(True)
