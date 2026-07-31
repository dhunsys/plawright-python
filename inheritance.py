# inherit Calculator2 syntax: child(parent):
from oops import Calculator2


class InhClass(Calculator2):
    num2 = 200
    def __init__(self,a,b):
        Calculator2.__init__(self,a,b) # call parent class constr
    def getCompleteData(self):
        return self.num2 + self.getData()


obj = InhClass(3, 4)
obj.setData(4)# call parent class method to initialize n3 var
print("Sum in child is ",obj.getCompleteData())
