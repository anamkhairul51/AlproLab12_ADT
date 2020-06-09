import math

class Vector2D(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector2D(self.x-other.x,self.y-other.y)

    def __mul__(self,other):
        return Vector2D(self.x*other.x,self.y*other.y)

    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

def main():
    v1 = Vector2D(1,2)
    v2 = Vector2D(3,4)
    v3 = v1+v2
    v4 = v1-v2
    v5 = v1*v2
    v6 = abs(v4)
    print(v1.x,v1.y)
    print(v2.x,v2.y)
    print(v3.x,v3.y)
    print(v4.x,v4.y)
    print(v5.x,v5.y)
    print(v6)
    print(v1 == v4)
    print(Vector2D(1,0) == Vector2D(1,0))
    
if __name__ == "__main__":
    main()
