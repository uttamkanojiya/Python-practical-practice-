#program to define and call a function
def outerfunction(a,b):
    square=a**2
    def addition (a,b):
        return a+b
    add=addition(a,b)
    return add +5
result=outerfunction(5,10)
print("The result is : \n",result)
