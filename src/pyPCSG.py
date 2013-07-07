#!/usr/bin/env python
import json
import os
import jsonpickle

class parameter(object):
	def __init__(self, name = ""):
		self.type = "parameter"
		self.name = name
	def __lt__(self,other):
		return __lt([self,other])

class element(object):
	def __init__(self, name = ""):
		self.type = "element"
		self.name = name
		self.construction = []

class operation(object):
	def __init__(self,name = "", elements = []):
		self.type = "operation"
		self.name = name
		self.elements = elements
		
class point(element):
	def __init__(self, location):
		element.__init__(self, name = "point")
		self.location = location
		self.construction = [self.location]
		
class primitive(element):
	def __init__(self, name = ""):
		element.__init__(self, name)
		self.location = [0,0,0]
		self.center = [0,0,0]
		self.construction = []
	def __add__(self, other):
		return union([self, other])
	def __sub__(self, other):
		return difference([self, other])

class union(operation, primitive): #union works on primitives
	def __init__(self, elements):
		operation.__init__(self, name = "union", elements = elements)

class __lt(operation):
	def __init__(self, elements):
		operation.__init__(self, name = "less than", elements = elements)
	
class __add(operation):
	def __init__(self, elements):
		operation.__init__(self, name = "add", elements = elements)

class difference(operation):
	def __init__(self, elements):
		operation.__init__(self, name = "difference", elements = elements)

class intersection(operation):
	def __init__(self,elements):
		operation.__init__(self, name = "intersection", elements = elements)

class extrude(operation):
	def __init__(self, elements, length):
		operation.__init__(self, name = "extrude", elements = elements)
		self.length = length

class square(primitive):
	def __init__(self, size = [0,0,0]):
		primitive.__init__(self, name = "square")
		self.size = size
		self.construction = [point([0,0]), point([size[0],0]), point([0,size[1]]), point([size[0], size[1]])]		

class cube(primitive):
	def __init__(self, size = [0,0,0]):
		primitive.__init__(self, name = "cube")
		self.size = size
		self.construction = [extrude(square(size), size[2])]

class cylinder(primitive):
	def __init__(self, radius = 0, height = 0):
		primitive.__init__(self, name = "cylinder")
		self.radius = radius
		self.height = height
		self.construction = []

class sphere(primitive):
	def __init__(self, radius = 0):
		primitive.__init__(self, name = "sphere")
		self.radius = radius
		self.construction = []

def export(obj, path):
	file = open(path, 'w')
	ext = os.path.splitext(path)[1]
	if ext == ".json":
		jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent = 4)
		file.write(jsonpickle.encode(obj, unpicklable=False))
		

param = parameter("a param")	
c = cube([0,0,3])
a = cube([1,1,1])
b = cube([10,10,10])
k = cylinder(radius = 1, height = 10)
sphere = sphere(radius = 2)
u = c+a+b-k
i = intersection([u,a])
export(i,"../tests/simple_test.json")
