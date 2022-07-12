'''
MEDIUM 69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        # I could find starting with 0, incrementing the value until one number surpases the objective 'x'
        low = 0
        top = x
        mid = 0
        while low < top:
            mid = (low+top) // 2
            if mid*mid <= x:
                low = mid + 1
            else:
                top = mid - 1
            print(low, mid, top)
        if low*low <= x:
            return low
        return low-1
