'''
MEDIUM 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

def longestSubString(ogString):
    mapa = {}
    indexBajo = 0
    maxLen = 0
    for indexAlto in range(len(ogString)):
        if ogString[indexAlto] not in mapa:
            print('El valor no estaba en el mapa c:')
            maxLen = max(maxLen, indexAlto-indexBajo+1)
        else:
            print("El ultimo index del char",ogString[indexAlto], "es", mapa[ogString[indexAlto]])
            if mapa[ogString[indexAlto]] < indexBajo:
                print("El char ", ogString[indexAlto], "no estaba en el mapa we :D")
                maxLen = max(maxLen, indexAlto-indexBajo+1)
            else:
                print("El char ", ogString[indexAlto], "estaba en el mapa we :(")
                indexBajo = mapa[ogString[indexAlto]] + 1
        mapa[ogString[indexAlto]] = indexAlto
        print(mapa)
    return maxLen

a = longestSubString('acbdbacd')
print(a)