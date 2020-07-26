class Node:
    def __init__(self, root, value):
        for i in value:
            self.val = i
            self.next = None
    #Values is a list()
    def setValues(self, root, values):
        curr = root
        for i in values:
            curr.next = Node(i)
            curr = curr.next
        return root
    #Print
    def printFunc(self, root):
        while root:
            print(root.val)
'''            
root = TreeNode(0)
curr = root
i = 1
while i < 10:
    curr.next = TreeNode(i)
    curr = curr.next
    i += 1
while root:
    print(root.val)
    root = root.next
'''