"""
EASY 226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   
  2     7
 /     / 
1   3 6   9
Output:

     4
   /   
  7     2
 /     / 
9   6 3   1
"""
from TreeNodeClass import TreeNode
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root