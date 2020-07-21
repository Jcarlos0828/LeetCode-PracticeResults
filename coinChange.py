class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if coins[0] > amount: return -1
        value = 0
        indexLow = 
        maxInd = len(coins)-1
        #Left = numDp, Right = numCoins
        dp = [[coins[0], 1]]
        while indexLow < maxInd:
            print("El valor", dp[value][0], "necesitAa", dp[value][1], "monedas")
            #Far right val < next index in coins
            if dp[value][0]+1 < coins[indexBig] or coins[indexBig] == -1:
                #print("PRIMER IF")
                dp.append([dp[value][0]+1, -1])
                print("El valor", dp[value][0], "necesitAAA", dp[value][1], "monedas")
                value += 1
                if dp[value][0] - coins[indexLow] != -1:
                    dp[value][1] = dp[value-(coins[indexLow])][1]+1
                #print("El valor", dp[value][0], "necesitaaaa", dp[value][1], "monedas")
            #We found a coin in the value sequence, the value will be = to 1
            else:
                dp.append([dp[value][0]+1, 1])
                value += 1
                indexLow = indexBig
                indexBig += 1
                
        while dp[value][0] != amount:
            
        return dp[value][1]      