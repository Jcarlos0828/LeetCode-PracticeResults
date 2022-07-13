'''
EASY 67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = []
        maxStr = b[::-1]
        minStr = a[::-1]
        if len(a) >= len(b):
            maxStr = a[::-1]
            minStr = b[::-1]
        i = 0
        carry = 0
        '''
        Truth table for line #23
        1 + (1 + 1) --> 11
        1 + (1 + 0) --> 10
        1 + (0 + 1) --> 10
        1 + (0 + 0) --> 01
        '''
        while i < len(minStr):
            digitA = int(maxStr[i])
            digitB = int(minStr[i])

            if carry:
                output.append(str(1 - (digitA ^ digitB)))
                carry = carry & (digitA | digitB)
            else:
                output.append(str(digitA ^ digitB))
                carry = digitA & digitB  # 1
            i += 1
        while i < len(maxStr):
            if carry:
                output.append(str((int(maxStr[i]) ^ carry)))
                carry = carry & int(maxStr[i])
            else:
                output.append(maxStr[i])
            i += 1
        if carry:
            output.append("1")
        return "".join(output[::-1])
