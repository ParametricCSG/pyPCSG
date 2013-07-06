#!/usr/bin/env python
import json
import os
import jsonpickle

class parameters(object):
	def __init__(self):
		self.type = "parameters"

class element(object):
	def __init__(self):
		self.type = "element"
		self.element = ""

class operation(object):
	def __init__(self):
		self.type = "operation"
		self.operation = ""
		
class point(element):
	def __init__(self):
		element.__init__(self)
		self.element = "point"
		self.location = [0,0,0]
		
class primitive(element):
	def __init__(self):
		element.__init__(self)
		self.location = [0,0,0]
		self.center = [0,0,0]

class union(operation):
	def __init__(self, elements):
		operation.__init__(self)
		self.type = "union"
		self.elements = elements

class difference(operation):
	def __init__(self, elements):
		operation.__init__(self)
		self.type = "difference"
		self.elements = elements

class intersection(operation):
	def __init__(self,elements):
		operation.__init__(self)
		self.operation = "intersection"
		self.elements = elements

class cube(primitive):
	def __init__(self, size = [0,0,0]):
		primitive.__init__(self)
		self.element = "cube"
		self.size = size
		
class object(parameters):
	def __init__(self):	
		self.parameters = parameters()
		self.construction
	def export(self,str):
		ext = os.path.splitext(str)[1]
		print ext
		if ext == ".json":
			p = self.params
			self.params = self.params.__dict__
			print json.dumps(self.__dict__, indent = 2)
	
c = cube()
a = cube()
u = union([c,a])
i = intersection([u,a])
jsonpickle.set_encoder_options('simplejson', sort_keys=False, indent = 4)
o = jsonpickle.encode(i, unpicklable=False)
print o
