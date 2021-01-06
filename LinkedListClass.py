from Node import Node
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.numNodes = 0

    def append(self, val):
        newNode = Node(val)
        if self.head.val is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode

    #Display the length of the linkedList
    def length(self):
        curr = self.head
        total = 0
        while curr:
            total += 1
            curr = curr.next
        print("Total number of Nodes in the LinkedList is:", total)
        return total

    #Display nodes value, one per line
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, "->")
            curr = curr.next

    #Method that creates a complete list from given values
    def createList(self, listNodes):
        for node in listNodes:
            self.append(node)
        #Returns head of LinkedList
        print("This is the head, dummie :P -->",self.head.val)
        return self.head
        