class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

def createList(lst=[]):
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for item in lst[1:]:
        current.next = Node(item)
        current = current.next

    return head

def printList(H):
    current_node = H
    while current_node:
        print(current_node,end=" ")
        current_node = current_node.next
    print(' ')


def mergeOrderesList(p, q):
    merged_head = None
    current = None

    while p and q:
        if p.data <= q.data:
            if merged_head is None:
                merged_head = Node(p.data)
                current = merged_head
            else:
                current.next = Node(p.data)
                current = current.next
            p = p.next
        else:
            if merged_head is None:
                merged_head = Node(q.data)
                current = merged_head
            else:
                current.next = Node(q.data)
                current = current.next
            q = q.next

    while p:
        current.next = Node(p.data)
        current = current.next
        p = p.next

    while q:
        current.next = Node(q.data)
        current = current.next
        q = q.next

    # Sort
    sorted_head = None
    current = merged_head

    while current:
        next_node = current.next

        if sorted_head is None or current.data <= sorted_head.data:
            current.next = sorted_head
            sorted_head = current
        else:
            sorted_current = sorted_head
            while sorted_current.next and sorted_current.next.data < current.data:
                sorted_current = sorted_current.next
            current.next = sorted_current.next
            sorted_current.next = current

        current = next_node

    return sorted_head

#################### FIX comand ####################   
# input only a number save in L1,L2
input_lists = input("Enter 2 Lists : ")
list1, list2 = input_lists.split()

L1 = list(map(int, list1.split(',')))
L2 = list(map(int, list2.split(',')))

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)