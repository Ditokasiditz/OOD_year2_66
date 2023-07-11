from math import pi

class Spherical:

    def __init__(self,r1):
        self.r = r1

    def changeR(self,r2):
        self.r = r2

    def findVolume(self):
        return (4/3)*pi*pow(self.r,3)

    def findArea(self):
        return 4*pi*pow(self.r,2)

    def __str__(self):
        return f'Radius ={self.r} Volumn = {Spherical.findVolume} Area = {Spherical.findArea}' 

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)