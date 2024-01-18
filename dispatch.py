# dispatch you to support method overloading in python
# for installation we need to run command : pip installl multipledispatch
from multipledispatch import dispatch
@dispatch (int,int)
def product(a,b):
    print(a*b)

@dispatch (int,int,int)
def product(a,b,c):
    print(a*b*c)
    
@dispatch(float,float,float)
def product(a,b,c):
    print(a*b*c)

product(2,3)
product(4,5,7)
