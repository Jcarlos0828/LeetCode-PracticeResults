'''
EASY 1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''
#Function definition modified from the Leetcode version to run on terminal in every computer
def runningSum(nums):
    myList = []
    acum = 0
    for i in nums:
        acum = acum + i
        myList.append(acum)
    return myList

#This is created to run on terminal in every computer
#Write the input with a space between numbers
nums = input("Add here your list ").split()
for i in range(0, len(nums)): 
    nums[i] = int(nums[i])
print(runningSum(nums))