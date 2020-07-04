'''
EASY 441. Arranging Coins

You have a total of n coins that you want to form in 
a staircase shape, where every k-th row must have exactly k coins.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = [0]
        count = 1
        def recur(n, count):  
            if n - count >= 0:
                rows[0] += 1
                count += 1
                recur(n-count+1, count)
            return
        recur(n, count)
        return rows[0]