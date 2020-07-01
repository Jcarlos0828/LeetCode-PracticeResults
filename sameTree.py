'''
EASY 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''

#Function made to copy and paste to run in the leetcode console
class Solution:
    #Solved searching that the trees are the same 
    def isSameTree(self, p, q) -> bool:
        
        
        if p is None and q is None:
            return True
        #Both conditions are to check if one node of both trees don't have either left or right son 
        if p is None:
            return False
        if q is None:
            return False
        #Check if the value is different
        if p.val != q.val:
            return False
        
        leftSame = self.isSameTree(p.left,q.left)
        rightSame= self.isSameTree(p.right,q.right)
        
        return leftSame and rightSame