class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)

    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt
    
    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.value)
            node = node.next
            while node != None:
                result += ", " + str(node.value)
                node = node.next
        result += "]"
        return result


data, k = input("Input : ").split('/')
data_list = list(map(int, data.split(' ')))
link1 = LinkedList()

for i in data_list:
    link1.append(i)


# print(link1)
current = link1.head
index = 0

if int(k) >= link1.size():
    print("Over length")
else:
    while current:
        if index % int(k) == 0:
            next_value = current.next.value if current.next else -1
            print(f"Now index {index} value is {current.value} next value is {next_value}")
        current = current.next
        index += 1