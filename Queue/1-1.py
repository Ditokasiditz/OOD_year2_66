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
    