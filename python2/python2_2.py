pi = 3.141592653589793
class Spherical:

    def __init__(self,r1):
        self.radius = r1

    def changeR(self,r2):
        self.radius = r2

    def findVolume(self):
        return (4/3)*pi*pow(self.radius,3)

    def findArea(self):
        return 4*pi*pow(self.radius,2)

    def __str__(self):
        return f'Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}' 

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)