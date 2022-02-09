import math;

class RegularPolygon:

   def __init__(self, n=3, side=1, x=0, y=0):
       self.__n = n
       self.__side = float(side)
       self.__x = float(x)
       self.__y = float(y)
      
   def getN(self):
       return self.__n
      
   def getSide(self):
       return self.__side
      
   def getX(self):
       return self.__x
  
   def getY(self):
       return self.__y
      
   def setN(self, n):
       self.__n = n
      
   def setSide(self, side):
       self.__side = side
      
   def setX(self, x):
       self.__x = x
  
   def setY(self, y):
       self.__y = y
      
   def getArea(self):
       return (self.__n * pow(self.__side,2)) / (4 * math.tan(math.pi/self.__n))
      
   def getPerimeter(self):
       return self.__n * self.__side
      

polygon1 = RegularPolygon()
print(polygon1.getArea())
print(polygon1.getPerimeter())


polygon2 = RegularPolygon(6, 4)    
print(polygon2.getArea())
print(polygon2.getPerimeter())


polygon3 = RegularPolygon(10, 4, 5.6, 7.8)
print(polygon3.getArea())
print(polygon3.getPerimeter())