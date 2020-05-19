class animals:
	"""public variable"""
	eyes = "2"
	def legs(self):
		print("I have 4 legs")

	"""Abstraction"""
	def eats(self):
		pass

class cat(animals):
	"""private variable"""
	__move = "Walk"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Rats")

class dog(animals):
	"""private variable"""
	__move = "Bark"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Fish")

class tiger(animals):
	__move = "Roar"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Animals")	

class lion(animals):
	"""private variable"""
	__move = "Roar"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Animals")

class rabbit(animals):
	"""private variable"""
	__move = "Walk"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat red chilli")

class elephant(animals):
	"""private variable"""
	__move = "Trumpet"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Small plants, Fruits")

class monkey(animals):
	"""private variable"""
	__move = "Jump"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Banana")

class snake(animals):
	"""private variable"""
	__move = "Crawl"
	def legs(self):
		print("I do not have legs")
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I drink milk")

class dinosaur(animals):
	"""private variable"""
	__move = "Similar to horns"
	def legs(self):
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Turtles")

class cheetah(animals):
	"""private variable"""
	__move = "Run Fast"
	def legs(self):	
		super().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat smaller hoofed animals")

def main():
	print("ABOUT CATS:")
	cats = cat()
	cats.legs()
	cats.eyes()
	cats.eats()
	print("I can " + cats._cat__move)
	print()
	print("ABOUT DOGS:")
	dogs = dog()
	dogs.legs()
	dogs.eyes()
	dogs.eats()
	print("I can " + dogs._dog__move)
	print()
	print("ABOUT TIGERS:")
	tigers = tiger()
	tigers.legs()
	tigers.eyes()
	tigers.eats()
	print("I can " + tigers._tiger__move)
	print()
	print("ABOUT LIONS:")
	lions = lion()
	lions.legs()
	lions.eyes()
	lions.eats()
	print("I can " + lions._lion__move)
	print()
	print("ABOUT RABBITS:")
	rabbits = rabbit()
	rabbits.legs()
	rabbits.eyes()
	rabbits.eats()
	print("I can " + rabbits._rabbit__move)
	print()
	print("ABOUT ELEPHANTS:")
	elephants = elephant()
	elephants.legs()
	elephants.eyes()
	elephants.eats()
	print("I can " + elephants._elephant__move)
	print()
	print("ABOUT MONKEYS:")
	monkeys = monkey()
	monkeys.legs()
	monkeys.eyes()
	monkeys.eats()
	print("I can " + monkeys._monkey__move)
	print()
	print("ABOUT SNAKES:")
	snakes = snake()
	snakes.legs()
	snakes.eyes()
	snakes.eats()
	print("I can " + snakes._snake__move)
	print()
	print("ABOUT DINOSAURS:")
	dinosaurs = dinosaur()
	dinosaurs.legs()
	dinosaurs.eyes()
	dinosaurs.eats()
	print("I can " + dinosaurs._dinosaur__move)
	print()
	print("ABOUT CHEETAHS:")
	cheetahs = cheetah()
	cheetahs.legs()
	cheetahs.eyes()
	cheetahs.eats()
	print("I can " + cheetahs._cheetah__move)


if __name__=="__main__":
	main()


