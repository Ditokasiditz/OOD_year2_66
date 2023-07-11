class Calculator :
  def __init__(self,x,y) :
    self.num1 = x
    self.num2 = y
  def add(self):
    return self.num1+self.num2

  def sub(self):
    return self.num1-self.num2

  def mul(self):
    return self.num1*self.num2

  def truediv(self):
    return self.num1/self.num2

  

x,y = input("Enter num1 num2 : ").split(",")

Cal1 = Calculator(int(x),int(y))


print(Cal1.add())
print(Cal1.sub())
print(Cal1.mul())
print(Cal1.truediv())