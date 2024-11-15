#program to understand the different type of arguments

#keyword arguments
def infor(name,age):
    print("Name:",name)
    print("Age:",age)
infor(age=19,name="uttam")

#default arguments
def func(name,age=87):
    print("Name:",name)
    print("Age:",age)
func(age=87,name="uttam")
func(name="uttam")

#Aribitary arguments
def greet(*names):
    for name in names:
        print("good morning",name)
greet("uttam","riya","yash","umesh")
