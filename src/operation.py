from textcad import component


class Union(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name="union", elements=elements)

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Difference(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self,
                                     name="difference",
                                     elements=elements)

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Intersection(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self,
                                     name="intersection",
                                     elements=elements)

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Extrude(component.Operation):
    def __init__(self, elements, length):
        component.Operation.__init__(self, name="extrude", elements=elements)
        self.length = length

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Hull(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name="hull", elements=elements)

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Rotate(component.Operation):
    def __init__(self, angle=0, axis=[0, 0, 0], elements=[]):
        component.Operation.__init__(self, name="rotate", elements=elements)
        self.angle = angle
        self.axis = axis

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Translate(component.Operation):
    def __init__(self, location=[0, 0, 0], elements=[]):
        component.Operation.__init__(self, name="translate", elements=elements)
        self.location = location

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Minkowski(component.Operation):
    def __init__(self, elements):
        component.Operation.__init__(self, name="minkowski", elements=elements)

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Mirror(component.Operation):
    def __init__(self, elements, axis=[]):
        component.Operation.__init__(self, name="mirror", elements=elements)
        self.axis = axis

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Scale(component.Operation):
    def __init__(self, elements, multiplier=[]):
        component.Operation.__init__(self, name="scale", elements=elements)
        self.multiplier = multiplier

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])


class Resize(component.Operation):
    def __init__(self, elements, newsize=[], auto=[]):
        component.Operation.__init__(self, name="resize", elements=elements)
        self.newsize = newsize
        self.auto = auto

    def __add__(self, other):
        return Union([self, other])

    def __sub__(self, other):
        return Difference([self, other])
