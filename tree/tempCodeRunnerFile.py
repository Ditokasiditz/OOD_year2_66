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


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    

    def below(self,below):
        #go to super left
        cur_node = self.root
        while True:
            if cur_node.left is None:
                break
            else :
                cur_node = cur_node.left

        #append to list
        list_belower = []
        
        while True:
            if cur_node < below:
                list_belower.append(cur_node.data)
                c 
            else:
                break
        


T = BST()


inp1,inp2 = input('enter input :').split('|')
inp_list = list(map(int,inp1.split(' ')))

for i in inp_list:          #append input the tree
    root = T.insert(i)
T.printTree(root)





# Python program to sort a
# stack using auxiliary stack.
 
# This function return the sorted stack
def sortStack ( stack ):
	tmpStack = createStack()
	while(isEmpty(stack) == False):
		
		# pop out the first element
		tmp = top(stack)
		pop(stack)

		# while temporary stack is not
		# empty and top of stack is
		# lesser than temp
		while(isEmpty(tmpStack) == False and
			int(top(tmpStack)) < int(tmp)):
			
			# pop from temporary stack and
			# push it to the input stack
			push(stack,top(tmpStack))
			pop(tmpStack)

		# push temp in temporary of stack
		push(tmpStack,tmp)
	
	return tmpStack

# Below is a complete running
# program for testing above
# function.

# Function to create a stack.
# It initializes size of stack
# as 0
def createStack():
	stack = []
	return stack

# Function to check if
# the stack is empty
def isEmpty( stack ):
	return len(stack) == 0

# Function to push an
# item to stack
def push( stack, item ):
	stack.append( item )

# Function to get top
# item of stack
def top( stack ):
	p = len(stack)
	return stack[p-1]

# Function to pop an
# item from stack
def pop( stack ):

	# If stack is empty
	# then error
	if(isEmpty( stack )):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack
def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end = ' ')
	print()

# Driver Code
stack = createStack()
push( stack, str(34) )
push( stack, str(3) )
push( stack, str(31) )
push( stack, str(98) )
push( stack, str(92) )
push( stack, str(23) )

print("Sorted numbers are: ")
sortedst = sortStack ( stack )
prints(sortedst)

# This code is contributed by
# Prasad Kshirsagar
