'''
Given two linked lists
1 -> 2 -> 3
4 -> 5 -> 6

return the sum of the 2 linked Lists value as follow
sum List1 = 321
sum List2 = 654
return sum List1 + sum List 2
'''


def sumLinkedLists(root1, root2):
    sum1 = sum2 = 0
    multiplied = 1
    curr1 = root1
    curr2 = root2
    while curr1 or curr2:
        if curr1:
            sum1 += curr1.val * multiplied
            curr1 = curr1.next
        if curr2:
            sum2 += curr2.val * multiplied
            curr2 = curr2.next
        multiplied *= 10
    return int(sum1 + sum2)