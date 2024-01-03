# #class
# class calculator:
#     def add(self,a,b):
#         print('sum:',a+b)
        
#     def sub(self,a,b):
        
#         print ('sub:',a-b)
    
#     def div(self,a,b):
#         if(b<0):
#             print("sorry!The value of b is less than 0")
#         else:
#             print("div:",a/b)
#     def mul(self,a,b):
#         print("mul:",a*b)
    
        
# obj=calculator()
# obj.add(5,4)
# obj.sub(16,3)
# obj.div(7,3)
# obj.mul(6,3)



#inheritance and constructor 

class Person:
    def __init__(self,fname,lname):
        self.firtname=fname
        self.lastname=lname
    def printname(self):
        print(self.firtname+' and '+self.lastname)
        
class student(Person):
    pass
x = Person("Aakash","Basanta")
x.printname()
y=student("Aakash","kandel")
y.printname()

