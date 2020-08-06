import NodeT

class TreeNode:
    def __init__(self):
        self.root = NodeT.NodeT()

        
    def append(self,val):
        if self.root.val == None:
            self.root.val = val
            return
        

    def appendRight(self,val):
        return

    #Receive a deque
    def append1(self, nodes):
        if self.root.val == None:
            self.root.val = nodes.popleft()

