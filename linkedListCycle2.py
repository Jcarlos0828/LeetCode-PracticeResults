"""
MEDIUM 142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: """ListNode""") -> """ListNode""":
        turtle = head
        index = 0
        dix = {}
        if not turtle: return
        while turtle:
            if turtle not in dix:
                dix[turtle] = index
            else:
                return turtle
            turtle = turtle.next
            index += 1
        return