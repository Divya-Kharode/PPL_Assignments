import turtle
import math

class shapes():
	def sides(self, no):
		pass
	def draw(self):
		pass

class conic(shapes):
	def sides(self):
		print("I dont have sides.")

class circle(conic):
	def __init__(self, no):
		self.__rad = no
	def sides(self):
		conic().sides()
	def draw(self, size):
		wn = turtle.Screen() 
		wn.setup(360,360)
		wn.delay(20)
		skk = turtle.Turtle()
		skk.circle(size)
		wn.clear()
	def area(self):
		self.area = 3.14 * self.__rad * self.__rad
		return self.area

class rectangle(shapes):
	def __init__(self, no1, no2):
		self.__height = no1
		self.__width = no2
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(0)
		skk.sety(10)
		skk.pendown()
		skk.forward(80)
		skk.left(90)

		skk.forward(40)
		skk.left(90)
  
		skk.forward(80) 
		skk.left(90)
  
		skk.forward(40)
		skk.left(90) 
		wn.clear()
	def area(self):
		return self.__height * self.__width

class square(shapes):
	def __init__(self, no1):
		self.__height = no1
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.forward(50)
		skk.left(90)

		skk.forward(50)
		skk.left(90)
  
		skk.forward(50) 
		skk.left(90)
  
		skk.forward(50)
		skk.left(90) 
		wn.clear()
	def area(self):
		return self.__height * self.__height

class triangle(shapes):
	def __init__(self, base, hei):
		self.__height = hei
		self.__base = base
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-50)
		skk.sety(50)
		skk.pendown()
		skk.forward(80)
		skk.left(120)

		skk.forward(80)
		skk.left(120)
  
		skk.forward(80) 
 
		wn.clear()
	def area(self):
		return self.__height * self.__base

class pentagon(shapes):
	def __init__(self, base, hei):
		self.__border = base
		self.__radius = hei
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-30)
		skk.sety(100)
		skk.pendown()
		for i in range(5):
			skk.forward(80)
			skk.right(72) 
 
		wn.clear()
	def area(self):
		return (5 * (int (self.__border) * int (self.__radius) )) / 2

class parallelogram(shapes):
	def __init__(self, base, hei):
		self.__base = base
		self.__height = hei
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-50)
		skk.sety(80)
		skk.pendown()
		for i in range(1, 3):
			skk.forward(100)
			skk.right(60)
			skk.forward(50)
			skk.right(120)
		wn.clear()
	def area(self):
		return self.__base*self.__height

class hexagon(shapes):
	def __init__(self, side):
		self.__s = side
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-50)
		skk.sety(80)
		skk.pendown()
		for i in range(6):
			skk.forward(100)
			skk.right(60)
		wn.clear()
	def area(self):
		return ((3 * math.sqrt(3) * (self.__s * self.__s)) / 2)


class ellipse(conic):
	def __init__(self, rad1, rad2):
		self.__a = rad1
		self.__b = rad2
	def sides(self):
		conic().sides()
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(400,400)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.up()
		skk.goto(-140,-75)
		skk.down()
		skk.seth(-45)
		skk.circle(200,90)
		skk.circle(100,90)
		skk.circle(200,90)
		skk.circle(100,90)
		wn.clear()
	def area(self):
		return 3.142 * self.__a * self.__b


class heptagon(shapes):
	def __init__(self, side):
		self.__s = side
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-50)
		skk.sety(80)
		skk.pendown()
		for i in range(7):
			skk.forward(100)
			skk.right(51.42)
		wn.clear()
	def area(self):
		return (1/2) * 7 * self.__s * 7.268

class rhombus(shapes):
	def __init__(self, dia1, dia2):
		self.__d1 = dia1
		self.__d2 = dia2
	def sides(self, no):
		print("I Have " + no + " sides.")
	def draw(self):
		wn = turtle.Screen() 
		wn.setup(360,360)
		skk = turtle.Turtle()
		wn.delay(20)
		skk.penup()
		skk.setx(-50)
		skk.sety(80)
		skk.pendown()
		for i in range(1, 3):
			skk.forward(100)
			skk.right(60)
			skk.forward(100)
			skk.right(120)
		wn.clear()
	def area(self):
		return (self.__d1 * self.__d2) / 2


def main():
	print("About Circle")
	circles = circle(10)
	circles.sides()
	circles.draw(50)
	area = circles.area()
	print("Area of circle is: " + str(area) )
	print()
	print("About Rectangle")
	rect = rectangle(10, 20)
	rect.sides("4")
	rect.draw()
	area = rect.area()
	print("Area of Rectangle is: " + str(area) )
	print()
	print("About Square")
	squ = square(20)
	squ.sides("4")
	squ.draw()
	area = squ.area()
	print("Area of Square is: " + str(area) )
	print()
	print("About Traingle")
	tri = triangle(5, 7)
	tri.sides("3")
	tri.draw()
	area = tri.area()
	print("Area of Triangle is: " + str(area) )
	print()
	print("About Pentagon")
	pent = pentagon(5, 3)
	pent.sides("5")
	pent.draw()
	area = pent.area()
	print("Area of Pentagon is: " + str(area) )
	print()
	print("About Parallelogram")
	para = parallelogram(5, 6)
	para.sides("4")
	para.draw()
	area = para.area()
	print("Area of Parallelogram is: " + str(area) )
	print()
	print("About Hexagon")
	hexa = hexagon(5)
	hexa.sides("6")
	hexa.draw()
	area = hexa.area()
	print("Area of Hexagon is: " + str(area) )
	print()
	print("About Ellipse")
	ell = ellipse(20, 30)
	ell.sides()
	ell.draw()
	area = ell.area()
	print("Area of Ellipse is: " + str(area) )
	print()
	print("About Heptagon")
	cyl = heptagon(10)
	cyl.sides("7")
	cyl.draw()
	area = cyl.area()
	print("Area of Heptagon is: " + str(area) )
	print()
	print("About Rhombus")
	rhom = rhombus(20, 30)
	rhom.sides("4")
	rhom.draw()
	area = rhom.area()
	print("Area of Rhombus is: " + str(area) )


if __name__ == "__main__":
	main()
