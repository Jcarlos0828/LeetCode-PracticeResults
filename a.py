'''
MEDIUM 337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, 
called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief 
realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / |
   2   3
    |   | 
     3   1

Output: 7  
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
'''
class Solution:
    def rob(self, root: '''TreeNode''') -> int:
        def postOrder(root):
            if not root:
                return 0, 0
            addL, noL = postOrder(root.left)
            addR, noR = postOrder(root.right)
            return root.val+noL+noR, max(addL,noL) + max(addR, noR)
        return max(postOrder(root))