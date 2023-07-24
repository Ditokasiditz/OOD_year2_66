class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1] if self.size()>0 else -1

    def push(self,tmp):
        self.items.append(tmp)

    def pop(self):
        return self.items.pop()

l = [[int(j) for j in i.split()] for i in input("Enter Input : ").split(",")]
s = Stack()
for i in l:
    # print("s_item",s.items)
    # print("i in l : ",i)
    while not s.isEmpty() and i[0] > s.top()[0]:
        print(s.pop()[1])
    s.push(i)