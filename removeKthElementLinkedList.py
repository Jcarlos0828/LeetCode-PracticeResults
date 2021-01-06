class Node:
    def __init__(self,val = None):

        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        

def removeK():
    head = LinkedList()
    head.val = 1
    head.next = Node(2)
    print(type(head.next))

removeK()