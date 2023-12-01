# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

class BST:
    def __init__(self):
        self.root = None 

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while cur != None:
                if data >= cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = Node(data)  # Fixed typo here
                        break
                    cur = cur.left
        return self.root

    def find_min(self):
        cur = self.root
        while True:
            if cur.left != None:
                cur = cur.left
            else:
                break
        return cur.data
            

    def find_max(self):
        cur = self.root
        while True:
            if cur.right != None:
                cur = cur.right
            else:
                break
        return cur.data


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)

print('Min :',T.find_min())
print('Max :',T.find_max())


                    

    