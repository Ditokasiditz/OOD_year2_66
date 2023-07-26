class Queue():

    def __init__(self, list=None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def enQueue(self, i):
        self.item.append(i)

    def deQueue(self):
        return self.item.pop(0) if not self.isEmpty() else None 

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []
    
    def index(self, value):
        try:
            return self.item.index(value)
        except ValueError:
            return -1

    def __str__(self):
        if not self.isEmpty():
            return " ".join(self.item)
        else:
            return "-1"
    
q1 = Queue()
inp = input("Enter Input : ").split(',')

for i in inp:
    if i[0] == 'E':
        q1.enQueue(i[2:])
        print(q1.size())
    elif i[0] == 'D':
        if not q1.isEmpty():
            print(q1.item[0], q1.index(q1.item[0]))
            q1.deQueue()
        else:
            None

print(q1)
print('Empty') if q1.isEmpty() else None 
