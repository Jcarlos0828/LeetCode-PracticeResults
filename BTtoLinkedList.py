'''
EASY 1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
'''
import collections
class Solution:
    def getDecimalValue(self, head: '''ListNode''') -> int:
        deque = collections.deque()
        index = 0
        while head:
            index += 1
            deque.append(head.val)
            head = head.next
        num = 0
        power = 0
        print(len(deque))
        while deque:
            num += deque.pop() * 2 ** power
            power += 1
        return num