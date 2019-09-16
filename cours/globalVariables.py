#global variable can be used by everyone, inside a function or outside
x = "merveilleux" #global

def myFunctionGlb():
    print("Python est " + x) 
    
myFunctionGlb()

#local variable with the same name inside myFunctionLcl()
def myFunctionLcl():
    x = "magnifique" #local
    print('Python est ' + x)

myFunctionLcl()

print('Python est ' + x)

"""
when you create a variable inside a function, this variable is local and can be used only inside this. for create a global variable inside a function use "global" keyword
"""

def myFunctionGlbKey():
    global y #global keyword
    y = "super"

myFunctionGlbKey()

print('Python est ' + y)
    
    
def modifyGlobal():
    global x
    x = "extraordinaire" #modify the global variable value.

modifyGlobal()

print('Python est ' + x)