# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        #Store the tree in a dict
        tree = {}
        acum = [0]
        self.preOrder(root, tree, acum)
        #After this point the tree and its node connections are stored
        print(tree)
        sub1 = 0
        sub2 = acum[0]
        pairs = list()
        for i in tree.keys():
            sub1 += i
            sub2 -= i
            pairs.append((sub1,sub2))
            for j in tree[i]:
                sub1 += j
                sub2 -= j
                pairs.append((sub1,sub2))
                sub1 -= j
                sub2 += j
            
                
        
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