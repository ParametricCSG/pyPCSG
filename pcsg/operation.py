import component

class Union(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name = "union", elements = elements)
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])

class Difference(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name = "difference", elements = elements)
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])

class Intersection(component.Operation):
    def __init__(self,elements):
        component.Operation.__init__(self, name = "intersection", elements = elements)
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])

class Extrude(component.Operation):
    def __init__(self, elements, length):
        component.Operation.__init__(self, name = "extrude", elements = elements)
        self.length = length
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])
        
class Hull(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name = "hull", elements = elements)
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])      

class Rotate(component.Operation):
    def __init__(self, angle = 0, axis=[0,0,0], elements):
        component.Operation.__init__(self, name = "rotate", elements = elements)
        self.angle = angle
        self.axis = axis
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])

class Translate(component.Operation):
    def __init__(self, location = [0,0,0], elements):
        component.Operation.__init__(self, name = "rotate", elements = elements)
        self.location = location
    def __add__(self, other):
        return Union([self, other])
    def __sub__(self, other):
        return Difference([self, other])
