class StackCalc:
    def __init__(self, lis = None):
        if lis is None:
            self.lis = []
        else:
            self.lis = lis
            
    def pop(self):
        return self.lis.pop()
    
    def push(self,i):
        self.lis.append(i)
        
    def size(self):
        return len(self.lis)
    
    def isEmpty(self):
        return len(self.lis) == 0
    
    def run(self, items ):
        self.bool = True
        for i in items:
            if i in '0123456789':
                self.push(i)
            elif i == '+' and self.lis[-2] :
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) + int(obj2)
                self.push(int(obj3))
            elif i == '-':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) - int(obj2)
                self.push(int(obj3))
            elif i == '*':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) * int(obj2)
                self.push(int(obj3))
            elif i == '/':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) / int(obj2)
                self.push(int(obj3))    
            elif i =="DUP":
                self.push(self.lis[-1])
            elif i =="POP":
                self.pop()
            elif i in "abcdefghijklmnopqrstuvwxyz":
               self.push(i)
               self.bool = False
               break
            else: 
                self.push(i)

    def getValue(self):
        if self.bool == False:
           return f'Invalid instruction: {self.lis[0]}'
        if len(self.lis) > 0:
            return self.lis[-1]
        else: 
            return '0'
        
print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())