class Solution:
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, data):
            self.items.append(data)

        def pop(self):
            if not self.isEmpty():
                return self.items.pop()
            else:
                return None

        def isEmpty(self):
            return len(self.items) == 0

        def peek(self):
            if not self.isEmpty():
                return self.items[-1]
            else:
                return None
        
        def __str__(self):
            s = ''
            if self.isEmpty():
                return s
            else:
                for c in self.items:
                    s += c
                return s

    def isValid(self, s: str):
        s1 = self.Stack()
        open_brac = ['(', '[', '{']
        close_brac = [')', ']', '}']
        
        for c in s:
            if c in open_brac:
                s1.push(c)
            elif c in close_brac:
                if s1.isEmpty() or open_brac.index(s1.peek()) != close_brac.index(c):
                    return False
                s1.pop()
            else:
                continue

        return s1.isEmpty()

sol = Solution()

print(sol.isValid('([]){()}'))
