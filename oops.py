#class

class Calculator:
    num = 100

    def getData(self):
        print("In get Data")


#create object. default constructor is invoked
obj = Calculator()
#call method
obj.getData()
#use memer var
print(obj.num)


#class with constr

class Calculator1:
    #class var
    num = 101

    #create constr
    def __init__(self):
        print("I am in constructor")

    def getData(self):
        print("In getData")


#create object. above constructor is invoked
obj = Calculator1()
#call method
obj.getData()
#use memer var
print(obj.num)


#class with constr and instance variable. instance var is declared withing constr/instance method
class Calculator2:
    #class var. call using class name
    num = 101

    #create constr
    def __init__(self, a, b):
        self.n1 = a  # n1 and n2 are instance variable
        self.n2 = b
        print("I am in parameterized constructor")

    def setData(self, c):
        self.n3 = c  # adding one more instance var

    def getData(self):
       return self.n1+self.n2+self.n3


#create object. above constructor is invoked
obj = Calculator2(2,3)
#call method
obj.setData(5)
print("The calculator 2 sum is",obj.getData())
#use memer var
print(Calculator2.num)
