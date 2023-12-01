# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

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
        if self.root == None:
            self.root = Node(data)
        else:
            cur_node = self.root 
            while cur_node != None:
                if data >= cur_node.data:
                    if cur_node.right == None:
                        cur_node.right = Node(data)
                        break
                    else:
                        cur_node = cur_node.right
                else:
                    if cur_node.left == None:
                        cur_node.left = Node(data)
                        break
                    else:
                        cur_node = cur_node.left
        return self.root

                    
            
    
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