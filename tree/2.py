class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            cur_node = self.root
            while True:
                if data < cur_node.data:
                    if cur_node.left is None:
                        cur_node.left = Node(data)
                        break
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.right = Node(data)
                        break
                    else :
                        cur_node = cur_node.right
        return self.root

    def findMin(self):
        cur_node = self.root
        while True:
            if cur_node.left is None:
                return cur_node
            else:
                cur_node = cur_node.left
    
    def findMax(self):
        cur_node = self.root
        while True:
            if cur_node.right is None:
                return cur_node
            else:
                cur_node = cur_node.right
            

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)

print('--------------------------------------------------')

print('Min :',T.findMin())
print('Max :',T.findMax())
