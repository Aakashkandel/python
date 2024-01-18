# write a program that takes a list of words as input and return a new list containing only the words that have more than 3 letters and start with the letter A as well as sorting alphabetically.

list1=["aakash","ant","modulal","asus","pratapsir","aaku","ambani"]
list2=[]
for word in list1:
 if (len(word)>5 and word[0]!='a'):
    list2.append(word)
print(list2)
list2.sort()
list2.reverse()
print(list2)
    
    # for word2 in list2:
    #     length=len(word)
    #     for i in range(0,length):
    #         for j in range(1,length):
    #             if()
    
    
    # create a class rectangle that has 2 attributes length and breadth ,the class should have a methode called area and perimeter that calculates area and perimeter of the rectangle.
    
class Rectangle:
    def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
    
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        print(perimeter)
    
    def area (self):
        area=self.length*self.breadth
        print(area)
    
obj= Rectangle(2,3)
obj.perimeter()
obj.area()

class square(Rectangle):
    pass

obj1=square(4,5)
obj1.area()

    