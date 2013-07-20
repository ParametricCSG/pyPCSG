class PCSG():
    def __init__(self, category = "", name = ""):
        self.name = name
        self.category = category

class Operation(PCSG):
    def __init__(self,name = "", elements = []):
        PCSG.__init__(self, category = "operation", name = name)
        self.elements = elements

class Element(PCSG):
    def __init__(self, name = "", construction = []):
        PCSG.__init__(self, category = "element", name = name)
        self.construction = construction

class Parameter(PCSG):
    def __init__(self, name = "", value = None):
        PCSG.__init__(self, category = "parameter", name = name)
        self.value = value

