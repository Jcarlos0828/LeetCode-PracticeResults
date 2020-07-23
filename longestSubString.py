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
    #Keep track of char found and the last index that was seen
    mapa = {}
    indexBajo = 0
    maxLen = 0
    #The right length of the window goes on
    for indexAlto in range(len(ogString)):
        #If the char is not in the dict, nothing happens, just sum the len
        if ogString[indexAlto] not in mapa:
            print('El valor no estaba en el mapa c:')
            maxLen = max(maxLen, indexAlto-indexBajo+1)
        
        else:
            print("El ultimo index del char",ogString[indexAlto], "es", mapa[ogString[indexAlto]])
            #If the last time the char was seen, is in the curr window, update the left length
            if mapa[ogString[indexAlto]] >= indexBajo:
                print("El char ", ogString[indexAlto], "estaba en el ventana we :(")
                indexBajo = mapa[ogString[indexAlto]] + 1
            #If that's not the case, it means that we saw the char in the past, but is not in the curr window
            else:
                print("El char ", ogString[indexAlto], "no estaba en la ventana we :D")
                maxLen = max(maxLen, indexAlto-indexBajo+1)

        mapa[ogString[indexAlto]] = indexAlto
        print(mapa)
    return maxLen

a = longestSubString('acbdbacd')
print(a)