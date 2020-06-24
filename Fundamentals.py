#Algorithms in python, this is more of a practice for myself

#Remove duplicates in a list
def removeDupl():
    arr=[1,2,3,5,7,9,6,4,8,3,2,6,1,5,7,3,5,9,2,6,7,3,4,2,1,1,5]
    arr = list(set(arr))
    return arr


#print(removeDupl())

# ----------
# Verify if a int/string is a palindrome
def isPalindrome(nums):
    # We can use .reverse() for lists
    return nums == int(str(nums)[::-1])
    

# if(isPalindrome(nums) ):
#    print("It is palindrome")
# else:
#    print("Isn't")
#----------------

#Do fibonacci series
def fibonacci(val1, val2):
    #Print the first 10 numbers
    count = 0
    while count < 10:
        print (val1)
        val1,val2 = val2, val1+val2
        count = count +1


#var1, var2 = 0, 1
#fibonacci(var1,var2)
#------------

#Check if a number is prime
def isPrime():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

#isPrime()
#------------
#PracticeCicles
def cyclesP():
    for n in range(10):
        print(n)
#cyclesP()
#----------------
arr = ['1','2','3','40']
arr2 = ['22','23','24']
newArr = []
#PracticeList.Extend()
def listaas():
    
    newArr.extend(arr)
    newArr.extend(arr2)
    print('Extended List: ', newArr)
#listaas()
#---------------

#PracticeList.insert()
#arr.insert(3,'100')
#arr.insert(3,'200')
#print(arr)
t = int(input())
for cases in range(t):
  m,n = map(int,input().split())
  if(m == 1):
    m = 2
    for i in range(m,n+1):
      for j in range(2,i):
        if(i % j == 0):
          break
      else:
        print(i)
print("\n")