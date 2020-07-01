'''
MEDIUM 1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
'''

#Function made to copy and paste to run in the leetcode console
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = 0
        #This will keep track of the levels, key = level, value = sum 
        dictionary = dict()
        self.preOrder(root, level, dictionary)
        print(dictionary)
        #Get the deepest level
        return dictionary[max(dictionary)]


    def preOrder(self, node, level, dictionary):
        
        #print("I am in node", node.val)
        #print("The level here is =",level,"\n")
        if level not in dictionary:
            print(level)
            dictionary[level] = node.val
        else:
            print(level)
            dictionary[level] += node.val
            
        if node is not None:
            if node.left:
                self.preOrder(node.left, level+1, dictionary)
            
            if node.right:
                self.preOrder(node.right, level+1, dictionary)