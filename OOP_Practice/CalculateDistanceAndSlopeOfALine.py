from math import sqrt


class Line:
	
	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2
		
	def distance(self):
		# coor1, coor2 - 2 tuples
		x = (self.coor2[0] - self.coor1[0]) ** 2
		y = (self.coor2[1] - self.coor1[1]) ** 2
		return (x+y)**0.5
	
	def slope(self):
		return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
	

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(f'Distance of the line with given co-ordinates is :: {li.distance()}')
print(f'Slope of the given line is :: {li.slope()}')
