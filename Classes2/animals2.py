class animals:
	"""public variable"""
	eyes = "2"
	def legs(self):
		print("I have 4 legs")

	"""Abstraction"""
	def eats(self):
		pass

	def get_home(self):
		pass

class domestic(animals):
	def get_home(self,derive = False):
		home = "Generally - At homes or live at stray places like streets, etc."
		if derive:
			return  home
		else:
			print(home)

class wild(animals):
	def get_home(self,derive = False):
		home = "Generally - At Forests or live at zoos, etc."
		if derive:
			return  home
		else:
			print(home)



class cat(domestic):
	"""private variable"""
	__move = "Walk"
	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Rats")

	def get_home(self):
		print(self.home)

class dog(domestic):
	"""private variable"""
	__move = "Bark"
	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Fish")

	def get_home(self):
		print(self.home)

class tiger(wild):
	__move = "Roar"
	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Animals")	

	def get_home(self):
		print(self.home)

class lion(wild):
	"""private variable"""
	__move = "Roar"

	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Animals")

	def get_home(self):
		print(self.home)

class rabbit(domestic):
	"""private variable"""
	__move = "Walk"

	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		domestic().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat red chilli")

	def get_home(self):
		print(self.home)

class elephant(wild):
	"""private variable"""
	__move = "Trumpet"

	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Small plants, Fruits")

	def get_home(self):
		print(self.home)

class monkey(wild):
	"""private variable"""
	__move = "Jump"

	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Banana")

	def get_home(self):
		print(self.home)

class snake(wild):
	"""private variable"""
	__move = "Crawl"
	def __init__(self):
		self.home = wild().get_home(True)

	def legs(self):
		print("I do not have legs")
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I drink milk")

	def get_home(self):
		print(self.home)

class dinosaur(wild):
	"""private variable"""
	__move = "Similar to horns"
	def __init__(self):
		self.home = wild().get_home(True)
	def legs(self):
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat Turtles")

	def get_home(self):
		print(self.home)

class cheetah(wild):
	"""private variable"""
	__move = "Run Fast"
	def __init__(self):
		self.home = wild().get_home(True)
	def legs(self):	
		wild().legs()
	def eyes(self):
		print("I have " + super().eyes + " eyes")

	"""Abstract method Overriding"""
	def eats(self):
		print("I eat smaller hoofed animals")

	def get_home(self):
		print(self.home)

def main():
	print("ABOUT CATS:")
	cats = cat()
	cats.legs()
	cats.eyes()
	cats.eats()
	cats.get_home()
	print("I can " + cats._cat__move)
	print()
	print("ABOUT DOGS:")
	dogs = dog()
	dogs.legs()
	dogs.eyes()
	dogs.eats()
	dogs.get_home()
	print("I can " + dogs._dog__move)
	print()
	print("ABOUT TIGERS:")
	tigers = tiger()
	tigers.legs()
	tigers.eyes()
	tigers.eats()
	tigers.get_home()
	print("I can " + tigers._tiger__move)
	print()
	print("ABOUT LIONS:")
	lions = lion()
	lions.legs()
	lions.eyes()
	lions.eats()
	lions.get_home()
	print("I can " + lions._lion__move)
	print()
	print("ABOUT RABBITS:")
	rabbits = rabbit()
	rabbits.legs()
	rabbits.eyes()
	rabbits.eats()
	rabbits.get_home()
	print("I can " + rabbits._rabbit__move)
	print()
	print("ABOUT ELEPHANTS:")
	elephants = elephant()
	elephants.legs()
	elephants.eyes()
	elephants.eats()
	elephants.get_home()
	print("I can " + elephants._elephant__move)
	print()
	print("ABOUT MONKEYS:")
	monkeys = monkey()
	monkeys.legs()
	monkeys.eyes()
	monkeys.eats()
	monkeys.get_home()
	print("I can " + monkeys._monkey__move)
	print()
	print("ABOUT SNAKES:")
	snakes = snake()
	snakes.legs()
	snakes.eyes()
	snakes.eats()
	snakes.get_home()
	print("I can " + snakes._snake__move)
	print()
	print("ABOUT DINOSAURS:")
	dinosaurs = dinosaur()
	dinosaurs.legs()
	dinosaurs.eyes()
	dinosaurs.eats()
	dinosaurs.get_home()
	print("I can " + dinosaurs._dinosaur__move)
	print()
	print("ABOUT CHEETAHS:")
	cheetahs = cheetah()
	cheetahs.legs()
	cheetahs.eyes()
	cheetahs.eats()
	cheetahs.get_home()
	print("I can " + cheetahs._cheetah__move)


if __name__=="__main__":
	main()


