"""
MEDIUM 1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""
import collections

#Using BFS
class Solution:
    
    def maxLevelSum(self, root: '''TreeNode''') -> int:

        queue = collections.deque()
        queue.append(root)
        level = 0
        outputLevel = 0
        maxSum = float('-inf')
        while queue:
            level += 1
            currSum = 0
            for _ in range(len(queue)):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                currSum += currNode.val
            if currSum > maxSum:
                maxSum = currSum
                outputLevel = level
        return outputLevel

#Using level by level
"""
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        childs = 0
        childsProcessed = 1
        
        maxVal = root.val
        sumLevel = 0
        levelMaxVal = 1
        currLevel = 1
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
                childs += 1
            if queue[0].right:
                queue.append(queue[0].right)
                childs += 1
            childsProcessed -= 1
            sumLevel += queue[0].val
            queue.popleft()
            if not childsProcessed:
                if sumLevel > maxVal:
                    levelMaxVal = currLevel
                    maxVal = sumLevel
                currLevel += 1
                sumLevel = 0
                childsProcessed = childs
                childs = 0
        return levelMaxVal
"""