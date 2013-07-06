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

class operation(object):
	def __init__(self,name = "", elements = []):
		self.type = "operation"
		self.name = name
		self.elements = []
		for elt in elements:
			if elt.type == self.type and elt.name == self.name:
				self.elements += elt.elements
			else:
				self.elements += [elt]
class point(element):
	def __init__(self):
		element.__init__(self, name = "point")
		self.location = [0,0,0]
		
class primitive(element):
	def __init__(self, name = ""):
		element.__init__(self, name)
		self.location = [0,0,0]
		self.center = [0,0,0]
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

class cube(primitive):
	def __init__(self,size = [0,0,0]):
		primitive.__init__(self, name = "cube")
		self.size = size
		
class cylinder(primitive):
	def __init__(self, radius = 0, height = 0):
		primitive.__init__(self, name = "cylinder")
		self.radius = radius
		self.height = height

class sphere(primitive):
	def __init__(self, radius = 0):
		primitive.__init__(self, name = "sphere")
		self.radius = radius

class object(object):
	def __init__(self, parameters = [], construction = [], requires = []):	
		self.parameters = parameters
		self.construction = construction
		self.requires = requires
	def export(self,str):
		file = open(str, 'w')
		ext = os.path.splitext(str)[1]
		if ext == ".json":
			jsonpickle.set_encoder_options('simplejson', sort_keys=False, indent = 4)
			file.write(jsonpickle.encode(self, unpicklable=False))
		

param = parameter("a param")	
c = cube([param,0,3])
a = cube([1,1,1])
b = cube([10,10,10])
k = cylinder(radius = 1, height = 10)
sphere = sphere(radius = 2)
u = c+a+b-k
i = intersection([u,a])
myObj = object(parameters = param, construction = i)
myObj.export("../tests/simple_test.json")
