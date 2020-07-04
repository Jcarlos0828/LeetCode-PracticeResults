'''
MEDIUM 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
].
'''

class Solution:
    def generateParenthesis(self, n: int):
        if n < 1:
            return [""]
        parenth = []
        #self.backtracking(word, countParL, countParR)
        
        #This function will only go trough valid cases
        def backtracking(word, countParL, countParR):
            #When reaching max number of (), store and go back
            if len(word) == (n * 2):
                parenth.append(word)
                return
            #If you can still write n '(', continue 
            if countParL < n:
                backtracking(word+'(',countParL+1, countParR)
            #If the number of ')' is equal to the '(' there's not case to continue searching
            if countParR < countParL:
                backtracking(word+")",countParL, countParR+1)
        backtracking("", 0, 0)
        return parenth