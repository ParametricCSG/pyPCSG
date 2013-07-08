from component import *
from operation import *

class Point(Element):
    def __init__(self, location):
        Element.__init__(self, name = "point")
        self.location = location
        self.construction = [self.location]
		
class Primitive(Element):
    def __init__(self, name = ""):
        Element.__init__(self, name)
        self.location = [0,0,0]
        self.center = [0,0,0]
        self.construction = []
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])
	    
class Square(Primitive):
    def __init__(self, size = [0,0,0]):
        Primitive.__init__(self, name = "square")
        self.size = size
        self.construction = [Point([0,0]), Point([size[0],0]), 
                             Point([0,size[1]]), Point([size[0], size[1]])]		

class Cube(Primitive):
    def __init__(self, size = [0,0,0]):
        Primitive.__init__(self, name = "cube")
        self.size = size
        self.construction = [Extrude([Square(size)], size[2])]

class Cylinder(Primitive):
    def __init__(self, radius = 0, height = 0):
        Primitive.__init__(self, name = "cylinder")
        self.radius = radius
        self.height = height
        self.construction = []

class Sphere(Primitive):
    def __init__(self, radius = 0):
        Primitive.__init__(self, name = "sphere")
        self.radius = radius
        self.construction = []
       
