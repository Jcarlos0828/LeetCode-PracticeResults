'''
MEDIUM 1339. Maximum Product of Splitted Binary Tree

Given a binary tree root. Split the binary tree into two subtrees 
by removing 1 edge such that the product of the sums of the subtrees are maximized.
Since the answer may be too large, return it modulo 10^9 + 7.
'''



class Solution:
    def maxProduct(self, root) -> int:
        #Store the tree in a dict
        tree = {}
        #Store the total value acumulated of the tree nodes
        acum = [0]
        self.preOrder(root, tree, acum)
        #Will store the biggest value
        bigVal = [0]
        self.postOrder(root, bigVal, acum)
        return bigVal[0] % 1000000007
        
    def preOrder(self, node, tree,  acum):
        tree[node.val] = node.val
        acum[0] += node.val
        tree[node.val] = list()
        
        if node:
            if node.left:
                tree[node.val].append(node.left.val)
                self.preOrder(node.left, tree, acum)
            if node.right:
                tree[node.val].append(node.right.val)
                self.preOrder(node.right, tree,acum)
            
    def postOrder(self, node, bigVal, acum):
        if node:
            subTreeSum = 0
            sumLeft = 0
            sumRight = 0
            if node.left:
                #Stores the sum of the left child of the node
                sumLeft = self.postOrder(node.left, bigVal, acum) 
            if node.right:
                #Stores the sum of the right child of the node
                sumRight = self.postOrder(node.right, bigVal, acum)
            
            #SubTreeSum stores the acum at the moment of doing the recursion
            subTreeSum = node.val + sumLeft + sumRight
            print("Suma:", subTreeSum, "\n")
            #Gets the multiplication of the 2 subtrees in question
            mult = ((acum[0] - subTreeSum) * subTreeSum)
            if mult > bigVal[0]:
                bigVal[0] = mult
            return subTreeSum
            
        return 0