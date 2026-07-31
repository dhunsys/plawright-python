def Hello():
    print("I am hello")


#call function
Hello()

def Hello(name):
    print("I am ", name)


#call function
Hello("MS")

#add 2 numbers

def add(a,b):
    print(a+b)

#call function
add(3,4)

#add 2 numbers and return

def add(a,b):
    return a+b


#call function
print("return", add(3,4))