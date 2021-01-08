'''
EASY 13. Roman to Integer

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        equi = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        total = 0
        for i in range(len(s)-1):
            if equi[s[i+1]] > equi[s[i]]:
                total -= equi[s[i]]
            else:
                total += equi[s[i]]
        total += equi[s[len(s)-1]]
        return total