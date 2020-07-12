'''
MEDIUM 904. Fruits into baskets

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, 
then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only 
carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
'''
#MY SOLUTON
class Solution:
    def totalFruit(self, tree: '''List[int]''')-> '''int ''':
        if len(tree) <= 2: 
            return len(tree)
        basket1 = tree[0]
        if basket1 != tree[1]:
            basket2 = tree[1]
            secondIndex = 1
        else: 
            basket2 = -1
            secondIndex = -1
        count = 2
        totalFruits = 2
        for i in range(2,len(tree)):
            print(tree[i])
            if basket2 == -1:
                if basket1 != tree[i]:
                    secondIndex = i
                    basket2 = tree[i]
                count += 1
                if count > totalFruits: totalFruits = count
                continue
            if tree[i] != basket1 and tree[i] != basket2:
                if count > totalFruits: totalFruits = count
                count = i - secondIndex + 1
                secondIndex = i
                basket1 = basket2
                basket2 = tree[i]
                
            elif tree[i] != basket2:
                secondIndex = i
                basket1 = basket2
                basket2 = tree[i]
                count += 1
                if count > totalFruits: totalFruits = count
                
            else:
                count += 1
                if count > totalFruits: totalFruits = count
                
        return totalFruits
#INSPIRED IN SOMEBODY ELSE SOLUTION
    #Using the sliding window technique
    def totalFruit1(self, tree):
        dictionary, i = {}, 0
        for j, VALUE in enumerate(tree):
            #If the key don't exists it creates it with default value 0 + 1
            dictionary[VALUE] = dictionary.get(VALUE, 0) + 1
            #The main condition is that you just want 2 values
            if len(dictionary) > 2:
                dictionary[tree[i]] -= 1
                #If you don't have more elements that means tha
                if dictionary[tree[i]] == 0: del dictionary[tree[i]]
                i += 1
        print(j)
        return j - i + 1
