'''
MEDIUM 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
import collections
class Solution:
    def levelOrder(self, root: '''TreeNode''') -> '''List[List[int]]''':
        tree = list()
        if not root:
            return tree
        def levelByLevel():
            nodeQueue = collections.deque()
            nodeQueue.append(root)
            childsInLevel = 0
            counterChangeLevel = 1
            storeAsList = list()
            
            while nodeQueue:
                if nodeQueue[0].left:
                    nodeQueue.append(nodeQueue[0].left)
                    childsInLevel += 1
                if nodeQueue[0].right:
                    nodeQueue.append(nodeQueue[0].right)
                    childsInLevel += 1
                storeAsList.append(nodeQueue[0].val)
                nodeQueue.popleft()
                counterChangeLevel -= 1
                if counterChangeLevel == 0:
                    counterChangeLevel = len(nodeQueue)
                    print(storeAsList)
                    tree.append(storeAsList.copy())
                    storeAsList.clear()
                    print('aA',storeAsList)
                    print('B', tree)
        levelByLevel()
        return tree
                    
                    