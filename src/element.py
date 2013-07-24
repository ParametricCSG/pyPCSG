from textcad.component import *
from textcad.operation import *

class Point(Element):
    def __init__(self, location):
        Element.__init__(self, name = "point")
        self.location = location
        self.construction = [self.location]

class Primitive(Element):
    def __init__(self, name = ""):
        Element.__init__(self, name)
        self.location = [0,0,0]
        self.rotation = _rotation()
        self.center = [0,0,0]
        self.color = [] #Set to RGBA array with vals 0-1. Alpha is optional, defaults to 1.
        self.construction = []
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])

class Square(Primitive):
    def __init__(self, size = [0,0,0]):
        Primitive.__init__(self, name = "square")
        self.size = size
        self.construction = []

class Cube(Primitive):
    def __init__(self, size = [0,0,0]):
        Primitive.__init__(self, name = "cube")
        self.size = size
        self.construction = []

class Cylinder(Primitive):
    def __init__(self, radius = 0, height = 0):
        Primitive.__init__(self, name = "cylinder")
        self.radius = radius
        self.height = height
        self.center = [1,1,0] #OpenSCAD default
        self.construction = []

class Hole(Primitive):
    def __init__(self, radius = 0, height = 0):
        Primitive.__init__(self, name = "hole")
        self.radius = radius
        self.height = height
        self.center = [1,1,0] #OpenSCAD default
        self.construction = []

class Cone(Primitive):
    def __init__(self, topRadius=0, bottomRadius=0, height=0):
        Primitive.__init__(self, name = "cone")
        self.topRadius = topRadius
        self.bottomRadius = bottomRadius
        self.height = height
        self.center = [1,1,0] #OpenSCAD default
        self.construction = []

class Ntube(Primitive):
    def __init__(self, sides=0, apothem=0, height=0):
        Primitive.__init__(self, name = "ntube")
        self.sides = sides
        self.apothem = apothem
        self.height = height
        self.center = [1,1,0] #OpenSCAD default
        self.construction = []

class Sphere(Primitive):
    def __init__(self, radius = 0):
        Primitive.__init__(self, name = "sphere")
        self.radius = radius
        self.center = [1,1,1] #OpenSCAD default
        self.construction = []

#Classes to make members scoped as needed       
class _rotation(object):
    def __init__(self):
        self.angle = 0
        self.axis = [0,0,0]
