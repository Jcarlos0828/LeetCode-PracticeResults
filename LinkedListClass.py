from Node import Node
    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        newNode = Node(val)
        curr = self.head
        if curr.val is None:
            self.head = newNode
        while curr.next != None:
            curr = curr.next
        curr.next = newNode

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            print("curr node", curr.val, "number #", total)
            total += 1
            curr = curr.next
        print("curr node", curr.val, "number #", total)
        return total
    
    def display(self):
        curr = self.head
        while curr.next != None:
            print(curr.val)
            curr = curr.next

    #Method that creates a complete list from given values
    def createList(self, listNodes):
        for node in listNodes:
            self.append(node)
        #Returns head of LinkedList
        print("This is the head, dummie :P -->",self.head.val)
        return self.head
        