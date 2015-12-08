class Animals(object):
	def __init__(self, name, breed, skin):
		self.name = name
		self.breed = breed
		self.skin = skin
	def has_fur(self):
		return self.skin == "fur"
	def is_a_dog(self):
		return self.breed == "dog"


Max = Animals("Max", "dog","fur")
Polly = Animals("Polly", "bird", "feathers")

print Max.has_fur()
print Polly.has_fur()
print Max.is_a_dog()
print Polly.is_a_dog()