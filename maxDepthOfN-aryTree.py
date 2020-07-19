"""
EASY 559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated 
by the null value (See examples). 
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        answer = [1]
        def dfs(root, currLevel):
            if root:
                if currLevel > answer[0]:   
                    answer[0] = currLevel
                for childs in root.children:
                    dfs(childs, currLevel+1)
        
        dfs(root, 1)
        return answer[0]