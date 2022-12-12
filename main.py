from math import sqrt 
class Rocket():

def _init_(self, x, y, z):

if type(x) == float and type(y) == float and type (2) == str;

self._x= x

self._y = y

self.name = z

else:

print( Object instantiation error")

def get(self):

return(self._x)

def gety (self):

return (self._y)

def get_distance (self, other _rocket):

distance = sqrt((self. _x-other_rocket getx())**2+(self. _y-other_rocket gety())*"2)

return distance

rocket = Rocket(0.0,0.0, "Titan")

rocket1 = Rocket (10.5,5.1, "Rhea")

distance = rocket.get_distance(rocket1)

print (rocketO.name,"and", rocket1.name,"are", distance, "apart.")