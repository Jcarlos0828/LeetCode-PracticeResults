'''
EASY 107. Binary Tree Level Order Traversal II

Given n pairs of parentheses, write a functionGiven a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

import collections
class Solution:
    def levelOrderBottom(self, root: '''TreeNode''') -> '''List[List[int]]''':
        processed = collections.deque()
        processed.append(root)
        tree = list()
        storeLevelNode = list()
        def levelByLevel():
            childs = 0
            counter = 1
            level = 0
            while processed:
                if processed[0].left: 
                    processed.append(processed[0].left)
                    childs += 1
                if processed[0].right:
                    processed.append(processed[0].right)
                    childs += 1
                storeLevelNode.append(processed[0].val)
                processed.popleft()
                counter -= 1    
                if counter == 0:
                    aux = storeLevelNode.copy()
                    tree.append(aux)
                    storeLevelNode.clear()
                    counter = len(processed)
                    level += 1
        if not root:
            return []
        levelByLevel()
        tree.reverse()
        return tree