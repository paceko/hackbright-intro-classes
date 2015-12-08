class Food(object):
	def __init__(self, instruction1, instruction2, instruction3):
		self.instruction1 = instruction1
		self.instruction2 = instruction2
		self.instruction3 = instruction3
	def print_recipe(self):
		print self.instruction1 
		print self.instruction2
		print self.instruction3
pb_apple = Food("cut apples", "place apples and some peanut butter on a platter with a knife", "eat")
cake = Food("combine ingredients", "cook in oven", "add whipped cream")


cake.print_recipe()
pb_apple.print_recipe()