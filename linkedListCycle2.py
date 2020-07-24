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
    #Explanation:
    #Fast travels twice of distance, we call x to the distance from head to where list cycles
    #We call y from the end of x to where fast and slow met, and Z from Y ends to Y starts
    def detectCycle(self, head: """ListNode""") -> """ListNode""":
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                print("El nodo donde se encontraron fue", slow.val)
                while head:
                    print("Actualmente el head vale", head.val, "y el slow vale", slow.val)
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return