class Stack:
    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1] if not Stack.is_empty() else None
    
    def is_empty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)
    
    def __str__(self):
        return "hello this is the end of the lecture"
    

s = Stack()
print(s.item)
# for ls in range(10):
#     s.push(ls)


print('the last element is :',s.peek())
print('check the list is empty',s.is_empty())
print('size of the stack:',s.size())
print(s.item)
s.pop()
print(s.item)
print(s)